import streamlit as st
from utils.api_client import login_api, register_api

st.set_page_config(page_title="FitMate | Teman Sehatmu", page_icon="🍏", layout="centered")

if "access_token" not in st.session_state:
    st.session_state["access_token"] = None
if "username" not in st.session_state:
    st.session_state["username"] = None

st.title("Selamat Datang di FitMate!")
st.markdown("FitMate dikembangkan sebagai *starting point* bagi kamu dalam memulai hidup sehat.")

if st.session_state["access_token"]:
    st.success(f"Halo, **{st.session_state['username']}**! Kamu sudah berhasil masuk.")
    st.write("Silakan gunakan menu navigasi di sebelah kiri (Sidebar) untuk mengakses Jurnal Pribadi, Kalkulator, dan Rekomendasi Menu.")

    if st.button("Logout", type="primary"):
        st.session_state["access_token"] = None
        st.session_state["username"] = None
        st.rerun()

else:
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        st.subheader("Masuk ke Akun")
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login", use_container_width=True)
            
            if submitted:
                res = login_api(username, password)
                if res and res.status_code == 200:
                    data = res.json()
                    st.session_state["access_token"] = data["access_token"]
                    st.session_state["username"] = username
                    st.success("Login berhasil!")
                    st.rerun()
                elif res and res.status_code == 401:
                    st.error("Username atau password salah.")
                else:
                    st.error("Gagal terhubung dengan server.")

    with tab2:
        st.subheader("Buat Akun Baru")
        with st.form("register_form"):
            new_username = st.text_input("Username")
            email = st.text_input("Email")
            
            col_r1, col_r2 = st.columns(2)
            with col_r1:
                age = st.number_input("Usia", min_value=10, max_value=100, step=1)
                height_cm = st.number_input("Tinggi Badan (cm)", min_value=100.0, step=1.0)
            with col_r2:
                gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
                activity_level = st.selectbox("Tingkat Aktivitas", ["sedentary", "light", "moderate", "active", "very_active"])
            
            new_password = st.text_input("Password", type="password")
            registered = st.form_submit_button("Daftar Sekarang", use_container_width=True)
            
            if registered:
                user_data = {
                    "username": new_username,
                    "email": email,
                    "age": age,
                    "gender": gender,
                    "height_cm": height_cm,
                    "activity_level": activity_level,
                    "password": new_password
                }
                res = register_api(user_data)
                if res and res.status_code == 200:
                    st.success("Registrasi berhasil! Silakan login.")
                else:
                    st.error("Registrasi gagal. Email atau Username mungkin sudah digunakan.")