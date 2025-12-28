import streamlit as st

# Single-line text input
name = st.text_input("Enter your name")

# Multi-line text input
bio = st.text_area("Enter your bio")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Dropdown
fruit = st.selectbox("Choose a fruit", ["Apple", "Banana", "Cherry"])

# Slider
age = st.slider("Select your age", 0, 100, 25)

# Button
if st.button("Submit"):
    st.write(f"Hello {name}, age {age}, you like {fruit}.")
    st.write("Bio:", bio)
    if uploaded_file:
        st.write("Uploaded file name:", uploaded_file.name)
