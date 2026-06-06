import streamlit as st
from utils.api_client import get_recipes_api

st.set_page_config(page_title="Rekomendasi Menu", page_icon="🥗", layout="wide")

st.title("Rekomendasi Menu Sehat")
st.write("Temukan berbagai pilihan resep makanan sehat lengkap dengan informasi nutrisinya.")

response = get_recipes_api()

if response and response.status_code == 200:
    recipes = response.json()
    
    if recipes:
        cols = st.columns(2)
        for index, recipe in enumerate(recipes):
            with cols[index % 2]:
                with st.container(border=True):
                    st.subheader(recipe["title"])
                    st.write(recipe["description"])
                    st.metric(label="Kalori Estimasi", value=f"{recipe['calories']} kkal")
                    
                    with st.expander("Lihat Resep Lengkap"):
                        st.markdown("**Bahan-bahan:**")
                        st.write(recipe["ingredients"])
                        st.markdown("**Cara Membuat:**")
                        st.write(recipe["instructions"])
    else:
        st.info("Belum ada resep yang tersedia di sistem saat ini.")
else:
    st.error("Gagal mengambil data resep dari server. Silakan coba lagi nanti.")