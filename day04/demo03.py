import os
import requests
import json
from dotenv import load_dotenv
import streamlit as st

st.title("My Chatbot")

load_dotenv()

api_key = "dummy-key"
url = "http://127.0.0.1:1234/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

user_prompt = st.chat_input("Ask anything:")

if user_prompt:
    with st.spinner("Thinking..."):
        req_data = {
            "model": "meta-llama-3.1-8b-instruct",  
            "messages": [{"role": "user", "content": user_prompt}]
        }

        response = requests.post(url, json=req_data, headers=headers)

        if response.status_code == 200:
            resp = response.json()
            st.write(resp[
                
                "choices"][0]["message"]["content"])
        else:
            st.error(f"Request failed: {response.status_code}")
