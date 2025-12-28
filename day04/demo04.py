import os
import requests
import json
import time
from dotenv import load_dotenv
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

req_data = {
    "model": "llama-3.1-8b-instant",   # ✅ correct Groq model
    "messages": [
        {"role": "system", "content": "You are experienced cricket commentator."},
        {"role": "user", "content": "Who is God of Cricket?"}
    ]
}

response = requests.post(
    url,
    data=json.dumps(req_data),
    headers=headers,
    verify=False
)

print("Status:", response.status_code)

resp = response.json()

print(resp["choices"][0]["message"]["content"])
