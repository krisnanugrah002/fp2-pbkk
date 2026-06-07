import streamlit as st
from utils.api_client import calculate_bmi_api, calculate_tdee_api

st.set_page_config(page_title="Kalkulator Kesehatan", page_icon="⚖️")

st.title("Kalkulator Kesehatan")
st.write("Hitung Body Mass Index (BMI) dan Total Daily Energy Expenditure (TDEE) kamu di sini.")

activity_mapping = {
    "sedentary": "Sedentary (Jarang bergerak)",
    "light": "Light (Olahraga ringan)",
    "moderate": "Moderate (Olahraga sedang)",
    "active": "Active (Olahraga berat)",
    "very_active": "Very Active (Sangat aktif)"
}

with st.form("kalkulator_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        usia = st.number_input("Usia (Tahun)", min_value=10, max_value=100, step=1)
        tinggi = st.number_input("Tinggi Badan (cm)", min_value=100.0, step=1.0)
        berat = st.number_input("Berat Badan (kg)", min_value=30.0, step=0.1)
        
    with col2:
        gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
        aktivitas_key = st.selectbox(
            "Tingkat Aktivitas Harian", 
            options=list(activity_mapping.keys()), 
            format_func=lambda x: activity_mapping[x]
        )
        
    hitung = st.form_submit_button("Hitung")

if hitung:
    bmi_res = calculate_bmi_api(berat, tinggi)
    tdee_res = calculate_tdee_api(berat, tinggi, usia, gender, aktivitas_key)
    
    if bmi_res and tdee_res and bmi_res.status_code == 200 and tdee_res.status_code == 200:
        bmi_data = bmi_res.json()
        tdee_data = tdee_res.json()
        
        st.success("Hasil Analisis Kesehatan Berhasil Dihitung!")
    
        m1, m2, m3 = st.columns(3)
        m1.metric(label="Skor BMI", value=f"{bmi_data['bmi']}")
        m2.metric(label="Kategori", value=f"{bmi_data['category']}")
        m3.metric(label="Kebutuhan Kalori (TDEE)", value=f"{tdee_data['tdee']} kkal/hari")
        
        st.info(f"**Metabolic Rate Dasar (BMR):** {tdee_data['bmr']} kkal. Ini adalah energi minimal yang dibutuhkan tubuhmu untuk bertahan hidup tanpa aktivitas tambahan.")
    else:
        st.error("Gagal terhubung dengan server.")