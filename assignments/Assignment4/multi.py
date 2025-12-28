import streamlit as st
import pandas as pd
from datetime import datetime
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="CSV Explorer App", layout="wide")

# ---------------- FILE NAMES ----------------
USERS_FILE = "users.csv"
HISTORY_FILE = "userfiles.csv"

# ---------------- AUTO CREATE CSV FILES ----------------
if not os.path.exists(USERS_FILE):
    pd.DataFrame(
        {
            "userid": [1, 2, 3],
            "username": ["12345678", "amit", "pallavi"],
            "password": ["pallavi@123", "amit@123", "pallavi"]
        }
    ).to_csv(USERS_FILE, index=False)

if not os.path.exists(HISTORY_FILE):
    pd.DataFrame(
        {
            "userid": [],
            "csv_name": [],
            "upload_time": []
        }
    ).to_csv(HISTORY_FILE, index=False)

# ---------------- LOAD DATA ----------------
users_df = pd.read_csv(USERS_FILE)
history_df = pd.read_csv(HISTORY_FILE)

# Strip extra spaces (avoid login issues)
users_df["username"] = users_df["username"].astype(str).str.strip()
users_df["password"] = users_df["password"].astype(str).str.strip()

# ---------------- SESSION STATE ----------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "userid" not in st.session_state:
    st.session_state.userid = None
if "username" not in st.session_state:
    st.session_state.username = ""

# ---------------- SIDEBAR MENU ----------------
st.sidebar.title("📌 Menu")

if not st.session_state.authenticated:
    menu = st.sidebar.radio("Navigation", ["Home", "Login", "Register"])
else:
    menu = st.sidebar.radio("Navigation", ["Explore CSV", "See History", "Logout"])

# ---------------- HOME ----------------
if menu == "Home":
    st.title("🏠 CSV Explorer Application")

    st.markdown("""
    ### 👋 Welcome!

    This web application allows users to **register, login, upload CSV files, and
    maintain upload history** using pandas and Streamlit.

    ---
    ### 🚀 Features
    - 🔐 User Authentication (Register / Login)
    - 📂 Upload and View CSV Files
    - 🕘 Track Upload History
    - 📊 Data Exploration using Pandas

    ---
    ### 🛠 Technologies Used
    - Python  
    - Streamlit  
    - Pandas  
    - CSV File Handling  

    > 📌 *Please login or register to continue.*
    """)

# ---------------- REGISTER ----------------
elif menu == "Register":
    st.title("📝 User Registration")

    st.markdown("""
    Please create a new account to access the application.

    **Guidelines:**
    - Username must be unique
    - Remember your credentials for future login
    """)

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Register"):
        if not username or not password:
            st.warning("⚠ Please fill all fields")
        elif username in users_df["username"].values:
            st.error("❌ Username already exists")
        else:
            new_id = users_df["userid"].max() + 1
            new_user = pd.DataFrame(
                [[new_id, username.strip(), password.strip()]],
                columns=["userid", "username", "password"]
            )
            users_df = pd.concat([users_df, new_user], ignore_index=True)
            users_df.to_csv(USERS_FILE, index=False)
            st.success("✅ Registration successful! You can now login.")

# ---------------- LOGIN ----------------
elif menu == "Login":
    st.title("🔐 User Login")

    st.markdown("""
    Enter your **registered username and password** to login.

    - Credentials are case-sensitive  
    - You must register before logging in  
    """)

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Login"):
        user = users_df[
            (users_df["username"] == username.strip()) &
            (users_df["password"] == password.strip())
        ]

        if not user.empty:
            st.session_state.authenticated = True
            st.session_state.userid = int(user.iloc[0]["userid"])
            st.session_state.username = username.strip()
            st.success("✅ Login successful")
            st.rerun()
        else:
            st.error("❌ Invalid username or password")

# ---------------- EXPLORE CSV ----------------
elif menu == "Explore CSV":
    st.title("📂 Explore CSV Files")
    st.write(f"👋 Welcome **{st.session_state.username}**")

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.subheader("📊 CSV Data Preview")
        st.dataframe(df)

        new_entry = pd.DataFrame(
            [[
                st.session_state.userid,
                uploaded_file.name,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ]],
            columns=["userid", "csv_name", "upload_time"]
        )

        history_df = pd.concat([history_df, new_entry], ignore_index=True)
        history_df.to_csv(HISTORY_FILE, index=False)

        st.success("✅ CSV uploaded and history saved")

# ---------------- HISTORY ----------------
elif menu == "See History":
    st.title("🕘 Upload History")

    user_history = history_df[
        history_df["userid"] == st.session_state.userid
    ]

    if user_history.empty:
        st.info("ℹ No upload history found")
    else:
        st.dataframe(user_history)

# ---------------- LOGOUT ----------------
elif menu == "Logout":
    st.session_state.authenticated = False
    st.session_state.userid = None
    st.session_state.username = ""
    st.success("👋 Logged out successfully")
    st.rerun()
