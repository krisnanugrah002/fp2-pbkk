import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

def get_headers():
    """Mengambil header otentikasi jika token tersedia di session state."""
    headers = {}
    if "access_token" in st.session_state and st.session_state["access_token"]:
        headers["Authorization"] = f"Bearer {st.session_state['access_token']}"
    return headers

# === AUTHENTICATION ===
def login_api(username, password):
    url = f"{BASE_URL}/api/auth/login"
    data = {"username": username, "password": password}
    try:
        response = requests.post(url, data=data)
        return response
    except requests.exceptions.ConnectionError:
        return None

def register_api(user_data):
    url = f"{BASE_URL}/api/auth/register"
    try:
        response = requests.post(url, json=user_data)
        return response
    except requests.exceptions.ConnectionError:
        return None

# === KALKULATOR KESEHATAN ===
def calculate_bmi_api(weight_kg, height_cm):
    url = f"{BASE_URL}/api/calculator/bmi"
    data = {"weight_kg": weight_kg, "height_cm": height_cm}
    try:
        return requests.post(url, json=data)
    except requests.exceptions.ConnectionError:
        return None

def calculate_tdee_api(weight_kg, height_cm, age, gender, activity_level):
    url = f"{BASE_URL}/api/calculator/tdee"
    data = {
        "weight_kg": weight_kg,
        "height_cm": height_cm,
        "age": age,
        "gender": gender,
        "activity_level": activity_level
    }
    try:
        return requests.post(url, json=data)
    except requests.exceptions.ConnectionError:
        return None

def get_weight_logs_api():
    url = f"{BASE_URL}/api/tracker/weight"
    try:
        return requests.get(url, headers=get_headers())
    except requests.exceptions.ConnectionError:
        return None

def create_weight_log_api(weight_kg):
    url = f"{BASE_URL}/api/tracker/weight"
    data = {"weight_kg": weight_kg}
    try:
        return requests.post(url, json=data, headers=get_headers())
    except requests.exceptions.ConnectionError:
        return None