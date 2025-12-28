from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

llm = init_chat_model(
    model="llama-3.1-8b-instant",  
    model_provider="openai",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

conversation = []

print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        break
    if not user_input:
        continue

    # Add user message to conversation
    user_msg = {"role": "user", "content": user_input}
    conversation.append(user_msg)

    # Get AI response
    llm_output = llm.invoke(conversation)
    print("AI:", llm_output.content)

    # Add AI response to conversation
    llm_msg = {"role": "assistant", "content": llm_output.content}
    conversation.append(llm_msg)
