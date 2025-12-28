import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read API key from .env file
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Session state initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "logged_out" not in st.session_state:
    st.session_state.logged_out = False


# ---------------- LOGIN PAGE ----------------
def login_page():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Fake authentication
        if username and password and username == password:
            st.session_state.logged_in = True
            st.session_state.logged_out = False
            st.success("Login Successful!")
            st.rerun()
        else:
            st.error("Invalid credentials (username and password must be same)")


# ---------------- WEATHER PAGE ----------------
def weather_page():
    st.title("Weather Information")

    city = st.text_input("Enter City Name")

    if st.button("Get Weather"):
        if city:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }

            response = requests.get(BASE_URL, params=params)

            if response.status_code == 200:
                data = response.json()
                st.subheader(f"Current Weather in {city.title()}")
                st.write("🌡 Temperature:", data["main"]["temp"], "°C")
                st.write("☁ Weather:", data["weather"][0]["description"].title())
                st.write("💧 Humidity:", data["main"]["humidity"], "%")
            else:
                st.error("City not found!")
        else:
            st.warning("Please enter a city name")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.logged_out = True
        st.rerun()


# ---------------- THANK YOU PAGE ----------------
def thank_you_page():
    st.title("Thank You!")
    st.success("You have been logged out successfully!")


# ---------------- PAGE ROUTING ----------------
if st.session_state.logged_in:
    weather_page()
elif st.session_state.logged_out:
    thank_you_page()
else:
    login_page()
