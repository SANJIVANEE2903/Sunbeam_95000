import streamlit as st
import requests
import os
from dotenv import load_dotenv

# -------------------------
# Page config MUST be first
# -------------------------
st.set_page_config(page_title="Groq vs LM Studio Chat", layout="wide")

# -------------------------
# Load environment variables
# -------------------------
load_dotenv()

# -------------------------
# Functions to query models
# -------------------------
def query_groq(prompt):
    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Groq Error: {response.status_code} - {response.text}"
    except requests.exceptions.SSLError:
        return "Network error. Check your connection."


def query_lm_studio(prompt):
    url = "http://127.0.0.1:1234/v1/chat/completions"

    payload = {
        "model": "meta-llama-3.1-8b-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            if "No models loaded" in response.text:
                return "LM Studio: No model loaded. Please load a model first."
            return f"LM Studio Error: {response.status_code} - {response.text}"
    except requests.exceptions.ConnectionError:
        return "LM Studio server not running."


# -------------------------
# Sidebar: Model selection
# -------------------------
st.sidebar.title("Select Model")
model_choice = st.sidebar.radio("Choose LLM:", ["Groq Cloud", "LM Studio"])

# -------------------------
# Sidebar: Chat history
# -------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.sidebar.subheader("Chat History")
for chat in st.session_state.chat_history:
    st.sidebar.markdown(f"**{chat['model_name']}**: {chat['user']}")
    st.sidebar.markdown(f"{chat['response']}")
    st.sidebar.markdown("---")

# -------------------------
# Main Chat UI
# -------------------------
st.title("Groq VS LM Studio Chat Bot")

user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get model response
    with st.chat_message("assistant"):
        if model_choice == "Groq Cloud":
            response = query_groq(user_input)
        else:
            response = query_lm_studio(user_input)

        st.markdown(f"**{model_choice}**\n\n{response}")

    # Save chat in session
    st.session_state.chat_history.append({
        "user": user_input,
        "response": response,
        "model_name": model_choice
    })

# -------------------------
# Display full chat history in main area
# -------------------------
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(chat["user"])

    with st.chat_message("assistant"):
        st.markdown(f"**{chat['model_name']}**\n\n{chat['response']}")
