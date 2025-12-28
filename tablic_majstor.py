import streamlit as st
import datetime

# 1. OSNOVNA PODEŠAVANJA
st.set_page_config(page_title="TAPI MAJSTOR PRO", layout="wide")

# 2. DIZAJN (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    .stButton>button {
        width: 100%; height: 70px; font-size: 20px !important;
        background-color: #1A1A1A; color: white; border: 2px solid #4F8BF9; border-radius: 12px;
    }
    .total-box {
        font-size: 32px; font-weight: bold; text-align: center;
        color: #00FF00; background: #111; padding: 12px; border-radius: 12px; border: 2px solid #333;
    }
    .istorija-okvir { background: #111; padding: 15px; border-left: 5px solid #4F8BF9; margin-bottom: 8px; border-radius: 5px; }
    h1, h2, h3 { text-align: center; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. INICIJALIZACIJA (Pamćenje podataka)
if 'strana' not in st.session_state: st.session_state.strana = 'pocetna'
if 'istorija_tablic' not in st.session_state: st.session_state.istor

