import streamlit as st
import datetime

# 1. PODEŠAVANJE STRANICE
st.set_page_config(page_title="TAPI MAJSTOR PRO", layout="wide")

# 2. KOMPLETAN DIZAJN (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
   
    /* Glavna dugmad - BELA SLOVA */
    .stButton>button {
        width: 100%; height: 80px; font-size: 26px !important;
        background-color: #1A1A1A; color: #FFFFFF !important;
        border: 2px solid #4F8BF9; border-radius: 15px; font-weight: bold;
    }
   
    .stButton>button:hover { border-color: #00FF00; color: #00FF00 !important; }

    /* Veliki brojevi za rezultat */
    .total-box {
        font-size: 42px; font-weight: bold; text-align: center;
        color: #00FF00; background: #111111; padding: 20px;
        border-radius: 15px; border: 2px solid #333333; margin-top: 10px;
    }

    /* Crta koja odvaja partije u tabliću */
    .partija-crta {
        border-bottom: 3px solid #444444;
        margin-top: 30px;
        margin-bottom: 30px;
    }

    /* Kartice u istoriji */
    .istorija-card {
        background: #111111; padding: 20px; border
