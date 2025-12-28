import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env file

api_key = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

user_prompt = input("Ask anything: ")

req_data = {
    "model": "llama-3.3-70b-versatile",
    "messages": [
        {"role": "user", "content": user_prompt}
    ]
}

response = requests.post(
    url,
    headers=headers,
    json=req_data,
    verify=False
)

# print("Status:", response.status_code)
# print(response.json())


print("Status:", response.status_code)

reply = response.json()["choices"][0]["message"]["content"]
print("\nAnswer:\n", reply)