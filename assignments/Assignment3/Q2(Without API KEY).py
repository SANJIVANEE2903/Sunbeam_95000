import streamlit as st
import requests

st.set_page_config(page_title="Login & Weather App", layout="centered")

# Session state initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "logged_out" not in st.session_state:
    st.session_state.logged_out = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in and not st.session_state.logged_out:
    st.title("Login Form")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Fake authentication: username == password
        if username and password and username == password:
            st.session_state.logged_in = True
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials (username and password must be same)")

# ---------------- WEATHER PAGE ----------------
elif st.session_state.logged_in:
    st.title("Weather Information")

    city = st.text_input("Enter city name")

    if st.button("Get Weather"):
        if city:
            try:
                # Free weather API (no API key required)
                url = f"https://wttr.in/{city}?format=j1"
                response = requests.get(url)
                data = response.json()

                current = data["current_condition"][0]

                st.subheader(f"Current Weather in {city}")
                st.write(f"Temperature: {current['temp_C']} °C")
                st.write(f"Weather: {current['weatherDesc'][0]['value']}")
                st.write(f"Humidity: {current['humidity']}%")
                st.write(f"Wind Speed: {current['windspeedKmph']} km/h")
            except Exception as e:
                st.error("Unable to fetch weather data")
        else:
            st.warning("Please enter a city name")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.logged_out = True
        st.rerun()

# ---------------- LOGOUT PAGE ----------------
elif st.session_state.logged_out:
    st.title("Thank You")
    st.success("Thanks for using the Weather App")
