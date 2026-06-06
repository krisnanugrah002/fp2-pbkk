import streamlit as st

st.set_page_config(
    page_title="FitMate | Teman Sehatmu",
    page_icon="🍏",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Selamat Datang di FitMate!")
st.markdown("FitMate dikembangkan sebagai *starting point* bagi kamu dalam memulai hidup sehat.")

tab1, tab2 = st.tabs(["Login", "Register"])

with tab1:
    st.subheader("Masuk ke Akun")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        
        if submitted:
            st.info("")

with tab2:
    st.subheader("Buat Akun Baru")
    with st.form("register_form"):
        new_username = st.text_input("Username")
        email = st.text_input("Email")
        new_password = st.text_input("Password", type="password")
        registered = st.form_submit_button("Daftar")
        
        if registered:
            st.info("")