import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

st.title("Groq Streaming Chatbot")

llm = ChatGroq(
    model="llama-3.1-8b-instant", 
    api_key=os.getenv("GROQ_API_KEY"),
    streaming=True,
)

def stream_response(prompt):
    for chunk in llm.stream(prompt):
        if chunk.content:
            yield chunk.content

user_input = st.chat_input("Say something")

if user_input:
    st.write_stream(stream_response(user_input))
