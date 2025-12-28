import streamlit as st
import datetime

# 1. OSNOVNA PODEŠAVANJA
st.set_page_config(page_title="TAPI MAJSTOR PRO", layout="wide")

# 2. DIZAJN (Bela slova, crna pozadina, crta između partija)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    .stButton>button {
        width: 100%; height: 75px; font-size: 24px !important;
        background-color: #1A1A1A; color: #FFFFFF !important;
        border: 2px solid #4F8BF9; border-radius: 12px; font-weight: bold;
    }
    .total-box {
        font-size: 38px; font-weight: bold; text-align: center;
        color: #00FF00; background: #111111; padding: 15px;
        border-radius: 15px; border: 2px solid #333333;
    }
    .partija-razmak {
        border-bottom: 2px solid #444;
        margin-top: 25px;
        margin-bottom: 25px;
    }
    .istorija-card {
        background: #111111; padding: 15px; border-left: 6px solid #4F8BF9;
        margin-bottom: 12px; color: white;
    }
    h1, h2, h3, p, label { color: white !important; text-align: center; }
    input { background-color: #222222 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. INICIJALIZACIJA (Sve opcije su ovde definisane)
if 'strana' not in st.session_state: st.session_state.strana = 'pocetna'
if 'istorija_tablic' not in st.session_state: st.session_state.istorija_tablic = []
if 'istorija_remi' not in st.session_state: st.session_state.istorija_remi = []

# Čuvamo imena u memoriji
if 'imena' not in st.session_state: st.session_state.imena = ["Igrač 1", "Igrač 2", "Igrač 3", "Igrač 4
