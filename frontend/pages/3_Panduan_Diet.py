import streamlit as st

st.set_page_config(page_title="Panduan Diet", page_icon="📖")

st.title("Panduan Metode Diet")
st.write("Pelajari berbagai metode pola makan sehat dan temukan rencana adaptasi praktis langkah demi langkah")

tab1, tab2 = st.tabs(["Intermittent Fasting", "Kalori Defisit"])

with tab1:
    st.header("Intermittent Fasting (Puasa Berkala)")
    st.write("Intermittent Fasting (IF) adalah pengaturan pola makan yang berfokus pada **kapan** kamu makan, bukan *apa* yang kamu makan.")
    
    st.subheader("Siapa yang Cocok?")
    st.write("Cocok untuk pemula yang ingin menjaga kadar gula darah dan tidak suka menghitung kalori makanan secara ketat.")
    
    st.subheader("Langkah Adaptasi Pemula")
    st.markdown("""
    * **Minggu 1:** Mulai dengan metode 12:12 (Puasa 12 jam, jendela makan 12 jam). Misalnya berhenti makan jam 8 malam, dan mulai sarapan jam 8 pagi.
    * **Minggu 2:** Tingkatkan perlahan ke 14:10.
    * **Minggu 3 & Seterusnya:** Terapkan metode populer 16:8 (Puasa 16 jam, jendela makan 8 jam).
    * **Tips:** Minum air putih, teh tawar, atau kopi hitam tanpa gula selama masa puasa tetap diperbolehkan!
    """)

with tab2:
    st.header("Kalori Defisit")
    st.write("Metode diet dengan cara mengonsumsi jumlah kalori yang lebih sedikit daripada yang dibakar oleh tubuh.")
    
    st.subheader("Langkah Adaptasi Pemula")
    st.markdown("""
    1. **Hitung TDEE:** Gunakan Kalkulator Kesehatan di aplikasi ini untuk mengetahui kebutuhan kalori harianmu.
    2. **Kurangi Kalori Secara Aman:** Kurangi sekitar 300 - 500 kalori dari TDEE kamu. Jangan mengurangkan kalori terlalu drastis agar metabolisme tidak rusak.
    3. **Tingkatkan Protein:** Konsumsi lebih banyak protein agar merasa kenyang lebih lama.
    4. **Tracking Makanan:** Gunakan Dashboard Jurnal FitMate untuk mencatat makanan harianmu.
    """)