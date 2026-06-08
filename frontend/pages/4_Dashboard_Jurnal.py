import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
from utils.api_client import (
    get_weight_logs_api, 
    create_weight_log_api,
    get_food_logs_api, 
    create_food_log_api,
    get_activity_logs_api,   
    create_activity_log_api    
)

st.set_page_config(page_title="Dashboard Jurnal", page_icon="📊", layout="wide")

st.title("Dashboard Jurnal")

if "access_token" not in st.session_state or not st.session_state["access_token"]:
    st.warning("Silakan melakukan login terlebih dahulu di halaman utama untuk mengakses Jurnal Pribadi.")
    st.stop()

tab_weight, tab_food, tab_activity = st.tabs(["Jurnal Berat Badan", "Jurnal Makanan", "Jurnal Aktivitas"])

with tab_weight:
    st.subheader("Entri Berat Badan Baru")
    with st.form("weight_log_form"):
        col1, col2 = st.columns([3, 1])
        with col1:
            weight_input = st.number_input("Berat Badan Hari Ini (kg)", min_value=20.0, max_value=200.0, value=60.0, step=0.1)
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            submit_weight = st.form_submit_button("Simpan Data", use_container_width=True)
            
        if submit_weight:
            res = create_weight_log_api(weight_input)
            if res and res.status_code == 200:
                st.success("Log berat badan berhasil disimpan!")
                st.rerun()
            else:
                st.error("Gagal menyimpan data ke server.")

    st.divider()
    st.subheader("Tren Perkembangan Berat Badan")
    weight_logs = get_weight_logs_api()
    
    if weight_logs and weight_logs.status_code == 200 and weight_logs.json():
        df_weight = pd.DataFrame(weight_logs.json())
        df_weight['log_date'] = pd.to_datetime(df_weight['log_date'])
        df_weight = df_weight.sort_values(by='log_date')
        df_weight['log_date'] = df_weight['log_date'].dt.strftime('%d-%m-%Y')
        
        fig = px.line(
            df_weight, 
            x="log_date", 
            y="weight_kg", 
            markers=True, 
            title="Grafik Berat Badan", 
            labels={"log_date": "Tanggal", "weight_kg": "Berat Badan (kg)"})
        fig.update_traces(line_color='#2E7D32', marker=dict(size=8))
        st.plotly_chart(fig, use_container_width=True)

        with st.expander("Lihat Detail Riwayat Data"):
            df_display = df_weight[['log_date', 'weight_kg']].rename(columns={
                'log_date': 'Tanggal', 
                'weight_kg': 'Berat (kg)'
            })
            
            df_display['Berat (kg)'] = df_display['Berat (kg)'].apply(lambda x: f"{x:g}")
            
            df_display.insert(0, 'No.', range(1, len(df_display) + 1))
   
            styled_df = df_display.style.set_properties(**{'text-align': 'center'}).set_table_styles([
                {'selector': 'th', 'props': [('text-align', 'center')]}
            ])
   
            st.dataframe(styled_df, hide_index=True, use_container_width=True)
    else:
        st.info("Belum ada riwayat data berat badan.")

with tab_food:
    st.subheader("Catat Konsumsi Makanan Harian")
    with st.form("food_log_form"):
        f_name = st.text_input("Nama Makanan / Minuman")
        f_cal = st.number_input("Kalori (kkal)", min_value=0.0, step=10.0)
        f_pro = st.number_input("Protein (gram)", min_value=0.0, step=1.0)
        submit_food = st.form_submit_button("Tambah Catatan Makanan")
                
    if submit_food:
        if f_name.strip() == "":
            st.error("Nama makanan tidak boleh kosong!")
        else:
            res_food = create_food_log_api(f_name, f_cal, f_pro)
        if res_food and res_food.status_code == 200:
            st.success("Catatan makanan berhasil ditambahkan!")
            st.rerun()
        else:
            st.error("Gagal menyimpan data makanan.")

    st.divider()
    food_logs = get_food_logs_api()

    if food_logs and food_logs.status_code == 200 and food_logs.json():
        df_food = pd.DataFrame(food_logs.json())
        df_food['log_date'] = pd.to_datetime(df_food['log_date']).dt.strftime('%Y-%m-%d')
    
        today_str = datetime.date.today().strftime('%Y-%m-%d')
        
        df_today = df_food[df_food['log_date'] == today_str]
        total_cal = df_today['calories'].sum()
        total_protein = df_today['protein_g'].sum()
                
        col_m1, col_m2 = st.columns(2)
        
        col_m1.metric("Total Kalori Hari Ini", f"{total_cal:g} kkal")
        col_m2.metric("Total Protein Hari Ini", f"{total_protein:g} g")
                
        st.markdown("<br>", unsafe_allow_html=True)
                
        df_display = df_food[['log_date', 'food_name', 'calories', 'protein_g']].rename(columns={
            'log_date': 'Tanggal', 
            'food_name': 'Nama Makanan', 
            'calories': 'Calories', 
            'protein_g': 'Protein (g)'
        })
                
        df_display['Calories'] = df_display['Calories'].apply(lambda x: f"{x:g}")
        df_display['Protein (g)'] = df_display['Protein (g)'].apply(lambda x: f"{x:g}")
        df_display.insert(0, 'No.', range(1, len(df_display) + 1))
                
        styled_df = df_display.style.set_properties(**{'text-align': 'center'}).set_table_styles([
            {'selector': 'th', 'props': [('text-align', 'center')]}
        ])
                
        st.dataframe(styled_df, hide_index=True, use_container_width=True)
    else:   
        st.info("Belum ada makanan yang dicatat.")

with tab_activity:
    st.subheader("Catat Aktivitas Olahraga Harian")

with st.form("activity_log_form"):
    a_name = st.text_input("Nama Olahraga / Aktivitas")
    a_cal = st.number_input("Estimasi Kalori Terbakar (kkal)", min_value=0.0, step=10.0)
    submit_activity = st.form_submit_button("Tambah Catatan Aktivitas")
                
    if submit_activity:
        if a_name.strip() == "":
            st.error("Nama olahraga tidak boleh kosong!")
        else:
            res_activity = create_activity_log_api(a_name, a_cal)
        if res_activity and res_activity.status_code == 200:
            st.success("Catatan aktivitas berhasil ditambahkan!")
            st.rerun()
        else:
            st.error("Gagal menyimpan data aktivitas. Pastikan koneksi backend lancar.")

    st.divider()
    activity_logs = get_activity_logs_api()
            
    if activity_logs and activity_logs.status_code == 200 and activity_logs.json():
        df_activity = pd.DataFrame(activity_logs.json())
        df_activity['log_date'] = pd.to_datetime(df_activity['log_date']).dt.strftime('%Y-%m-%d')

        today_str = datetime.date.today().strftime('%Y-%m-%d')
        df_act_today = df_activity[df_activity['log_date'] == today_str]
        total_burned = df_act_today['calories_burned'].sum()
                
        st.metric("Total Kalori Terbakar Hari Ini", f"{total_burned:g} kkal")
        st.markdown("<br>", unsafe_allow_html=True)

        df_act_display = df_activity[['log_date', 'activity_name', 'calories_burned']].rename(columns={
            'log_date': 'Tanggal', 
            'activity_name': 'Nama Olahraga', 
            'calories_burned': 'Kalori Terbakar (kkal)'
        })
                
        df_act_display['Kalori Terbakar (kkal)'] = df_act_display['Kalori Terbakar (kkal)'].apply(lambda x: f"{x:g}")
        df_act_display.insert(0, 'No.', range(1, len(df_act_display) + 1))
            
        styled_act_df = df_act_display.style.set_properties(**{'text-align': 'center'}).set_table_styles([
            {'selector': 'th', 'props': [('text-align', 'center')]}
        ])
                
        st.dataframe(styled_act_df, hide_index=True, use_container_width=True)
    else:
        st.info("Belum ada aktivitas olahraga yang dicatat.")
        