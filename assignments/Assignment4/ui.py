# 1. Make a chat bot like UI. Input a message from user and reply it back, but
# display the reply using st.write_stream(). Use delay to show chatlike effect.

import streamlit as st
import time

st.set_page_config(page_title="Simple Chatbot", layout="centered")
st.title("💬 Chat Bot UI")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

def stream_response(text):
    for word in text.split():
        yield word + " "
        time.sleep(0.3)   # delay for chat-like effect

if user_input:
    # Store and display user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.write(user_input)

    # Bot response (echo reply)
    bot_reply = f"You said: {user_input}"

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    with st.chat_message("assistant"):
        st.write_stream(stream_response(bot_reply))
