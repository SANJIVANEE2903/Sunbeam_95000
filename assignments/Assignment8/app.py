import streamlit as st
import os
import re
import requests
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.agents.middleware import wrap_model_call

# -------------------------------
# Load Environment Variables
# -------------------------------
load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(page_title="LangChain Multi-Agent Chat", layout="wide")
st.title("LangChain Multi-Agent Chat")

# -------------------------------
# Session State for Chat History
# -------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------------
# Original Functions with Docstrings
# -------------------------------
def calculator_fn(expression: str) -> str:
    """Evaluate a math expression and return the result as a string."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


def read_file_fn(filepath: str) -> str:
    """Read the contents of a local text file and return it as a string."""
    try:
        filepath = filepath.replace("\\", "/")  # Windows-safe
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"


def get_weather_fn(city: str) -> str:
    """Fetch current weather (temperature, humidity, wind speed) for a given city."""
    if not OPENWEATHER_API_KEY:
        return "❌ Weather API key not set."
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    try:
        data = requests.get(url).json()
        if data.get("cod") != 200:
            return f"❌ Could not fetch weather for {city}."
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        return f"🌡 Temp: {temp}°C\n💧 Humidity: {humidity}%\n🌬 Wind: {wind} m/s"
    except Exception as e:
        return f"❌ Error fetching weather: {e}"

# -------------------------------
# Wrap Functions as Tools
# -------------------------------
calculator = tool(calculator_fn)
read_file = tool(read_file_fn)
get_weather = tool(get_weather_fn)

tools = [calculator, read_file, get_weather]

# -------------------------------
# Middleware for Logging
# -------------------------------
@wrap_model_call
def model_logging(request, handler):
    st.write("--- BEFORE MODEL CALL ---")
    response = handler(request)
    st.write("--- AFTER MODEL CALL ---")
    return response

# -------------------------------
# Initialize LLM (LM Studio)
# -------------------------------
llm = init_chat_model(
    model="phi3-mini-128k-instruct",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="dummy"
)

# -------------------------------
# Create Agent
# -------------------------------
agent = create_agent(
    model=llm,
    tools=tools,
    middleware=[model_logging],
    system_prompt="""
You are a tool-using assistant.

Rules:
- Use calculator for math.
- Use read_file for file reading.
- Use get_weather for weather queries.
- Keep answers short and clear.
"""
)

# -------------------------------
# Helper: Extract File Path
# -------------------------------
def extract_path(text: str):
    """Extract a Windows or Linux file path from a string."""
    match = re.search(r"(?:[A-Za-z]:)?/[^\s]+", text)
    return match.group(0) if match else None

# -------------------------------
# Streamlit User Input
# -------------------------------
user_input = st.text_input("You:")

if st.button("Send") and user_input.strip():
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # -------------------------------
    # Auto-handle file reading
    # -------------------------------
    if user_input.lower().startswith("read file"):
        path = extract_path(user_input)
        if not path:
            ai_msg = "❌ Could not detect a valid file path."
        else:
            ai_msg = read_file.invoke({"filepath": path})
        st.session_state.chat_history.append({"role": "assistant", "content": ai_msg})

    # -------------------------------
    # Auto-handle weather queries
    # -------------------------------
    elif "weather" in user_input.lower():
        city_match = re.search(r"weather of ([a-zA-Z\s]+)", user_input.lower())
        city = city_match.group(1) if city_match else user_input
        ai_msg = get_weather.invoke({"city": city.strip()})
        st.session_state.chat_history.append({"role": "assistant", "content": ai_msg})

    # -------------------------------
    # All other inputs handled by the agent
    # -------------------------------
    else:
        with st.spinner("Thinking..."):
            result = agent.invoke({"messages": st.session_state.chat_history})
            ai_msg = result["messages"][-1].content
            st.session_state.chat_history.append({"role": "assistant", "content": ai_msg})

# -------------------------------
# Display Chat History
# -------------------------------
st.divider()
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**AI:** {msg['content']}")
