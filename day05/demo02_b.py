import streamlit as st
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

st.title("LangChain Streaming Chatbot (Groq)")

llm = init_chat_model(
    model="llama-3.1-8b-instant",   # ✅ Supported Groq model
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

user_input = st.chat_input("Say something...")

if user_input:
    result = llm.stream(user_input)

    # ---- RUNNING STREAM (manual) ----
    msg_box = st.empty()
    output = ""
    for chunk in result:
        if chunk.content:
            output += chunk.content
            msg_box.markdown(output)

    # ---- ALTERNATIVE STREAM (kept commented) ----
    # st.write_stream(chunk.content for chunk in llm.stream(user_input) if chunk.content)
