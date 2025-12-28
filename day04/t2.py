load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
"Authorization": f"Bearer {api_key}",
"Content-Type": "application/json"
}
data = {
"model": "meta-llama-3.1-8b-instruct",
"messages": [
{"role": "system", "content": "You are a helpful tutor who
explains concepts step by step."},
{"role": "user", "content": "Explain what an API is using a
restaurant analogy."}
]
}
response = requests.post(url, headers=headers,
data=json.dumps(data))
print(response.json())