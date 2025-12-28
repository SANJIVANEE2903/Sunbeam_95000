from dotenv import load_dotenv
import os
import requests

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

API_KEY = os.getenv("API_KEY")

print("API_KEY:", API_KEY)


def get_current_weather(city):
    """Fetch weather for a city."""
    if not API_KEY:
        raise ValueError("API_KEY not found. Check your .env file")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )
    response = requests.get(url)
    print("Status:", response.status_code)
    return response.json()


def pretty_print_weather(weather):
    """Display weather info nicely."""
    if "main" in weather:
        print("Temperature:", weather["main"]["temp"], "°C")
        print("Humidity:", weather["main"]["humidity"], "%")
        print("Wind Speed:", weather["wind"]["speed"], "m/s")
        print("Cloud:", weather["clouds"]["all"], "%")
        print("Weather:", weather["weather"][0]["description"])
    else:
        print("Error:", weather.get("message", "Something went wrong"))
