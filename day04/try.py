import json
import requests
url = "http://localhost:1234/v1/chat/completions"
headers = {
"Content-Type": "application/json",
"Authorization": "Bearer not-needed"
}
data = {
"model": "meta-llama-3.1-8b-instruct",
"messages": [
{"role": "user", "content": "Explain what quantization is in simple terms."}
]
}
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())