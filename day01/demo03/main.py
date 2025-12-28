
import requests

api_key = "3de90f5481b6aad759d034d72f5da8bf"  # Put your correct API key here

city = input("Enter city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
weather = response.json()

print("status:", response.status_code)
print("API Response:", weather)

if response.status_code == 200:
    print("Temperature:", weather["main"]["temp"])
    print("Humidity:", weather["main"]["humidity"])
    print("Wind Speed:", weather["wind"]["speed"])
else:
    print("Error:", weather.get("message", "Unknown error"))

