import streamlit as st

st.set_page_config(page_title="Kalkulator Kesehatan", page_icon="⚖️")

st.title("Kalkulator Kesehatan")
st.write("Hitung Body Mass Index (BMI) dan Total Daily Energy Expenditure (TDEE) kamu di sini.")

with st.form("kalkulator_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        usia = st.number_input("Usia (Tahun)", min_value=10, max_value=100, step=1)
        tinggi = st.number_input("Tinggi Badan (cm)", min_value=100.0, step=1.0)
        berat = st.number_input("Berat Badan (kg)", min_value=30.0, step=0.1)
        
    with col2:
        gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
        aktivitas = st.selectbox("Tingkat Aktivitas Harian", [
            "Sedentary (Jarang bergerak)",
            "Light (Olahraga ringan)",
            "Moderate (Olahraga sedang)",
            "Active (Olahraga berat)",
            "Very Active (Sangat aktif)"
        ])
        
    hitung = st.form_submit_button("Hitung")

if hitung:
    st.warning("")