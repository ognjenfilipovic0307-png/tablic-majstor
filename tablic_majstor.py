import streamlit as st
import datetime

# 1. OSNOVNA PODEŠAVANJA STRANICE
st.set_page_config(page_title="TAPI MAJSTOR PRO", layout="wide")

# 2. KOMPLETAN DIZAJN (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
   
    .stButton>button {
        width: 100%; height: 75px; font-size: 24px !important;
        background-color: #1A1A1A; color: #FFFFFF !important;
        border: 2px solid #4F8BF9; border-radius: 12px; font-weight: bold;
    }
   
    .stButton>button:hover { border-color: #00FF00; color: #00FF00 !important; }

    .total-box {
        font-size: 38px; font-weight: bold; text-align: center;
        color: #00FF00; background: #111111; padding: 15px;
        border-radius: 15px; border: 2px solid #333333; margin-top: 10px;
    }

    .istorija-card {
        background: #111111; padding: 15px; border-left: 6px solid #4F8BF9;
        margin-bottom: 12px; border-radius: 8px; color: #FFFFFF; font-size: 18px;
    }

    h1, h2, h3, p, label, .stMarkdown { color: white !important; text-align: center; }
    .stRadio label { color: white !important; font-size: 20px !important; }
   
    input { background-color: #222222 !important; color: white !important; }
   
    /* Stil za crtu između partija */
    .partija-razmak {
        border-bottom: 2px solid #333;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. INICIJALIZACIJA MEMORIJE
if 'strana' not in st.session_state: st.session_state.strana = 'pocetna'
if 'istorija_tablic' not in st.session_state: st.session_state.istorija_tablic = []
if 'istorija_remi' not in st.session_state: st.session_state.istorija_remi = []
if 'imena' not in st.session_state: st.session_state.imena = ["Igrač 1", "Igrač 2", "Igrač 3", "Igrač 4"]
if 'ime_grupe_a' not in st.session_state: st.session_state.ime_grupe_a = "Grupa A"
if 'ime_grupe_b' not in st.session_state: st.session_state.ime_grupe_b = "Grupa B"

# Inicijalizacija poena
if 't_skor' not in st.session_state:
    akteri = ["Grupa A", "Grupa B", "Igrač 1", "Igrač 2", "Igrač 3", "Igrač 4"]
    st.session_state.t_skor = {a: {"p": [0]*7, "r": [0]*7} for a in akteri}
if 'r_skor' not in st.session_state:
    akteri = ["Grupa A", "Grupa B", "Igrač 1", "Igrač 2", "Igrač 3", "Igrač 4"]
    st.session_state.r_skor = {a: 0 for a in akteri}

def promeni_ekran(ime_strane):
    st.session_state.strana = ime_strane
    st.rerun()

# --- EKRAN 1: POČETNI MENI ---
if st.session_state.strana == 'pocetna':
    st.markdown("<h1>🏆 TAPI MAJSTOR</h1>", unsafe_allow_html=True)
    if st.button("🎮 IGRAJ"): promeni_ekran('izbor_igre')
    if st.button("📊 PREGLED STATISTIKE"): promeni_ekran('izbor_pregleda')
   
    with st.expander("⚙️ PODEŠAVANJE IMENA (IGRAČI I GRUPE)"):
        st.write("--- Imena Igrača ---")
        for i in range(4):
            st.session_state.imena[i] = st.text_input(f"Igrač {i+1}:", st.session_state.imena[i], key=f"set_i_{i}")
        st.write("--- Imena Grupa ---")
        st.session_state.ime_grupe_a = st.text_input("Ime prve grupe:", st.session_state.ime_grupe_a)
        st.session_state.ime_grupe_b = st.text_input("Ime druge grupe:", st.session_state.ime_grupe_b)

# --- EKRAN 2: IZBOR IGRE ---
elif st.session_state.strana == 'izbor_igre':
    st.title("Šta igramo?")
    if st.button("🃏 TABLIĆ"): promeni_ekran('igra_tablic')
    if st.button("🎴 REMI"): promeni_ekran('igra_remi')
    if st.button("⬅️ NAZAD"): promeni_ekran('pocetna')

# --- EKRAN 3: IZBOR PREGLEDA ---
elif st.session_state.strana == 'izbor_pregleda':
    st.title("Pregled rezultata")
    if st.button("📜 ISTORIJA TABLIĆA"): promeni_ekran('prikaz_tablic')
    if st.button("📜 ISTORIJA REMIJA"): promeni_ekran('prikaz_remi')
    if st.button("⬅️ NAZAD"): promeni_ekran('pocetna')

# --- EKRAN 4: TABLIĆ ---
elif st.session_state.strana == 'igra_tablic':
    st.title("🃏 TABLIĆ (6 PARTIJA)")
    izbor_f = st.radio("Format:", ["2 Igrača", "4 Igrača", "2 Grupe"], horizontal=True, key="t_f")
   
    if izbor_f == "2 Igrača":
        akteri_t = [st.session_state.imena[0], st.session_state.imena[1]]
    elif izbor_f == "2 Grupe":
        akteri_t = [st.session_state.ime_grupe_a, st.session_state.ime_gru

