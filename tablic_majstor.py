import streamlit as st
import datetime

st.set_page_config(page_title="TAPI MAJSTOR PRO", layout="wide")

# PROFESIONALNI CSS
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    .stButton>button { width: 100%; height: 65px; font-size: 20px !important; background-color: #1A1A1A; color: white; border: 2px solid #4F8BF9; border-radius: 12px; transition: 0.3s; }
    .stButton>button:hover { border-color: #00FF00; background-color: #222; }
    .total-box { font-size: 35px; font-weight: bold; text-align: center; background-color: #0E1117; padding: 15px; border: 3px solid #00FF00; border-radius: 15px; color: #00FF00; }
    .partija-red { background-color: #111; padding: 15px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #333; }
    .istorija-card { background-color: #1A1A1A; padding: 15px; border-radius: 10px; border-left: 8px solid #4F8BF9; margin-bottom: 10px; font-size: 18px; }
    h1, h2, h3 { text-align: center; color: white !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stNumberInput input { background-color: #222 !important; color: white !important; font-size: 22px !important; text-align: center !important; }
    </style>
    """, unsafe_allow_html=True)

# SISTEMSKA LOGIKA
if 'strana' not in st.session_state: st.session_state.strana = 'pocetna'
if 'istorija_tablic' not in st.session_state: st.session_state.istorija_tablic = []
if 'istorija_remi' not in st.session_state: st.session_state.istorija_remi = []

# --- POČETNI EKRAN ---
if st.session_state.str
