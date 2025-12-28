from dotenv import load_dotenv
import os
import requests
from langchain.chat_models import init_chat_model

# Load environment variables
load_dotenv()

# Get API keys
weather_api_key = os.getenv("OPENWEATHER_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

if not weather_api_key:
    raise ValueError("OPENWEATHER_API_KEY not found in environment variables")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

# Initialize LLM
llm = init_chat_model(
    model="llama-3.1-8b-instant",
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=groq_api_key
)

print("Type 'exit' to quit.\n")

while True:
    city = input("Enter city name (or type 'exit' to quit): ").strip()
    if city.lower() == "exit":
        break
    if not city:
        continue

    # Fetch current weather
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching weather: {response.json().get('message', 'Unknown error')}")
        continue

    weather_data = response.json()
    print(f"\nRaw weather data for {city}:")
    print(weather_data)

    # Ask LLM to explain the weather
    llm_input = f"""
    Explain the following weather data for {city} in simple English:

    {weather_data}
    """
    explanation = llm.invoke(llm_input)
    print("\nWeather Explanation:")
    print(explanation.content)
    print("\n" + "-"*50 + "\n")
