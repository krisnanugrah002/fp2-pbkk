import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

def get_headers():
    headers = {}
    if "access_token" in st.session_state and st.session_state["access_token"]:
        headers["Authorization"] = f"Bearer {st.session_state['access_token']}"
    return headers

def login_api(username, password):
    url = f"{BASE_URL}/api/auth/login"
    data = {"username": username, "password": password}
    try:
        return requests.post(url, data=data)
    except requests.exceptions.ConnectionError:
        return None

def register_api(user_data):
    url = f"{BASE_URL}/api/auth/register"
    try:
        return requests.post(url, json=user_data)
    except requests.exceptions.ConnectionError:
        return None

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

def get_recipes_api():
    url = f"{BASE_URL}/api/recipes/"
    try:
        return requests.get(url, headers=get_headers())
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

def get_food_logs_api():
    url = f"{BASE_URL}/api/tracker/food"
    try:
        return requests.get(url, headers=get_headers())
    except requests.exceptions.ConnectionError:
        return None

def create_food_log_api(food_name, calories, protein_g):
    url = f"{BASE_URL}/api/tracker/food"
    data = {"food_name": food_name, "calories": calories, "protein_g": protein_g}
    try:
        return requests.post(url, json=data, headers=get_headers())
    except requests.exceptions.ConnectionError:
        return None

def get_activity_logs_api():
    url = f"{BASE_URL}/api/tracker/activity"
    try:
        return requests.get(url, headers=get_headers())
    except requests.exceptions.ConnectionError:
        return None

def create_activity_log_api(activity_name, calories_burned):
    url = f"{BASE_URL}/api/tracker/activity"
    data = {"activity_name": activity_name, "calories_burned": calories_burned}
    try:
        return requests.post(url, json=data, headers=get_headers())
    except requests.exceptions.ConnectionError:
        return None