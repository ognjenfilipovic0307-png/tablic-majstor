import streamlit as st
import datetime

# PODEŠAVANJA
st.set_page_config(page_title="TAPI MAJSTOR", layout="wide")

# DIZAJN
st.markdown("""
    <style>
    .stApp { background-color: #0d0d0d; color: white; }
    .stButton>button { width: 100%; height: 60px; font-size: 18px !important; border-radius: 10px; }
    .total-box { font-size: 30px; font-weight: bold; text-align: center; color: #00FF00; background: #1a1a1a; padding: 10px; border-radius: 10px; border: 1px solid #333; }
    .header-text { text-align: center; color: #4F8BF9; }
    </style>
    """, unsafe_allow_html=True)

# INICIJALIZACIJA (Sprečava greške pri učitavanju)
if 'strana' not in st.session_state: st.session_state.strana = 'pocetna'
if 'istorija_tablic' not in st.session_state: st.session_state.istorija_tablic = []
if 'istorija_remi' not in st.session_state: st.session_state.istorija_remi = []
if 'imena' not in st.session_state: st.session_state.imena = ["Igrač 1", "Igrač 2", "Igrač 3", "Igrač 4"]

def idi_na(nova_strana):
    st.session_state.strana = nova_strana
    st.rerun()

# --- 1. POČETNI MENI ---
if st.session_state.strana == 'pocetna':
    st.markdown("<h1 class='header-text'>🏆 TAPI MAJSTOR</h1>", unsafe_allow_html=True)
    if st.button("🎮 NOVA IGRA"): idi_na('biraj_igru')
    if st.button("📊 PREGLED TABELA"): idi_na('pregled_izbor')
   
    with st.expander("⚙️ PROMENI IMENA"):
        for i in range(4):
            st.session_state.imena[i] = st.text_input(f"Ime {i+1}", st.session_state.imena[i])

# --- 2. BIRANJE IGRE ---
elif st.session_state.strana == 'biraj_igru':
    st.title("Šta igramo?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🃏 TABLIĆ"): idi_na('tablic')
    with col2:
        if st.button("🎴 REMI

if st.session_state.str

