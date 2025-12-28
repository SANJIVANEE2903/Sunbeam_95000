import requests

api_key = "91f27bcd38b8f3fae4cfe39c578b4b20"  

city = input("Enter city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
weather = response.json()

print("status:", response.status_code)
print("API Response:", weather)   # <-- THIS IS REQUIRED

if response.status_code == 200:
    print("Temperature:", weather["main"]["temp"])
    print("Humidity:", weather["main"]["humidity"])
    print("Wind Speed:", weather["wind"]["speed"])
else:
    print("Error:", weather.get("message", "Unknown error"))
