from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

# ---------------- Tools ----------------

def calculator(expression: str) -> str:
    """Solve arithmetic expressions with numbers only"""
    try:
        allowed = "0123456789+-*/(). "
        if not all(c in allowed for c in expression):
            return "Error: Invalid characters"
        return str(eval(expression, {"__builtins__": {}}))
    except Exception:
        return "Error: Invalid arithmetic expression"

def get_weather(city: str) -> str:
    """Return current temperature, wind, humidity"""
    try:
        api_key = os.getenv("OPENWEATHER_API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
        resp = requests.get(url, timeout=10).json()
        if "main" not in resp or "wind" not in resp:
            return "Error: City not found"
        return json.dumps({
            "temperature": resp["main"]["temp"],
            "humidity": resp["main"]["humidity"],
            "wind_speed": resp["wind"]["speed"]
        })
    except Exception:
        return "Error: Cannot fetch weather"

# ---------------- Chat Loop ----------------

print("✅ Phi-3 Mini Assistant (type 'exit' to quit)\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        break

    # Simple routing logic
    if any(word in user_input.lower() for word in ["solve", "*", "+", "-", "/", "(", ")"]):
        result = calculator(user_input.replace("solve", "").strip())
    elif any(word in user_input.lower() for word in ["weather", "temperature", "humidity", "wind"]):
        city = user_input.lower().replace("weather in", "").strip()
        result = get_weather(city)
    else:
        result = "I can only calculate math expressions or get current weather."

    print("AI:", result)
