import streamlit as st
import time
from datetime import datetime

# 1. KONFIGURACIJA I "GAMING" DIZAJN
st.set_page_config(page_title="Tablić & Remi Master", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); color: white; }
   
    /* Stil za velika početna dugmad */
    div.stButton > button:first-child {
        height: 150px;
        font-size: 50px !important;
        border-radius: 20px;
        border: 2px solid #00c6ff;
        background: rgba(255, 255, 255, 0.1);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: #00c6ff !important;
        color: black !important;
        transform: scale(1.02);
    }
   
    /* Stil za kartice sa skorom */
    .stat-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 20px;
        border-left: 5px solid #00c6ff;
        text-align: center;
        margin-bottom: 15px;
    }
   
    /* Istorija - lepši izgled */
    .history-card {
        background: rgba(0, 0, 0, 0.3);
        padding: 10px;
        border-radius: 10px;
        margin-top: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# PAMĆENJE ISTORIJE
if 'istorija' not in st.session_state:
    st.session_state.istorija = []

# --- POČETNI EKRAN (VELIKE IKONE) ---
if 'igra_odabrana' not in st.session_state:
    st.markdown("<h1 style='text-align: center; margin-bottom: 50px;'>🃏 IZABERI IGRU</h1>", unsafe_allow_html=True)
   
    c1, c2 = st.columns(2)
    with c1:
        if st.button("♠️\nTABLIĆ"):
            st.session_state.igra_odabrana = "Tablić"
            st.rerun()
    with c2:
        if st.button("♥️\nREMI"):
            st.session_state.igra_odabrana = "Remi"
            st.rerun()
    st.stop()

# --- PODEŠAVANJE IGRAČA ---
if 'podaci' not in st.session_state:
    st.title(f"Postavke za {st.session_state.igra_odabrana}")
    format_igre = st.radio("Format:", ["U grupama (2 na 2)", "Svako za sebe"])
   
    with st.form("setup"):
        if format_igre == "U grupama (2 na 2)":
            c1, c2 = st.columns(2)
            with c1: e1 = st.text_input("Ekipa 1:", "Tijana i Miloš")
            with c2: e2 = st.text_input("Ekipa 2:", "Rade i Bojana")
            if st.form_submit_button("POKRENI"):
                st.session_state.podaci = {"format": "ekipe", "skorovi": {e1: 0, e2: 0}, "imena": [e1, e2]}
                st.rerun()
        else:
            imena = st.text_input("Unesi imena (odvojena zarezom):", "Ognjen, Rade, Bojana, Tijana")
            if st.form_submit_button("POKRENI"):
                lista = [i.strip() for i in imena.split(",")]
                st.session_state.podaci = {"format": "solo", "skorovi": {i: 0 for i in lista}, "imena": lista}
                st.rerun()
    st.stop()

# --- GLAVNA IGRA ---
st.title(f"🎮 {st.session_state.igra_odabrana}")

# Prikaz trenutnih rezultata
cols = st.columns(len(st.session_state.podaci["imena"]))
for i, ime in enumerate(st.session_state.podaci["imena"]):
    with cols[i]:
        st.markdown(f'<div class="stat-card"><h3>{ime}</h3><h1 style="font-size: 60px;">{st.session_state.podaci["skorovi"][ime]}</h1></div>', unsafe_allow_html=True)
        poeni = st.number_input(f"Dodaj poene:", step=1, key=f"p_{ime}")
        if st.button(f"Upiši za {ime.split()[0]}", key=f"btn_{ime}"):
            st.session_state.podaci["skorovi"][ime] += poeni
            st.rerun()

st.divider()

# --- DUGME ZA KRAJ I ČUVANJE ---
if st.button("🏁 ZAVRŠI PARTIJU I SAČUVAJ"):
    skorovi = st.session_state.podaci["skorovi"]
    pobednik = max(skorovi, key=skorovi.get)
    datum_vreme = datetime.now().strftime("%d.%m.%Y. u %H:%M")
   
    rezultat_detalji = " | ".join([f"{k}: {v}" for k, v in skorovi.items()])
   
    st.session_state.istorija.append({
        "datum": datum_vreme,
        "igra": st.session_state.igra_odabrana,
        "detalji": rezultat_detalji,
        "pobednik": pobednik
    })
   
    st.balloons() # Slavljenički baloni!
    st.success(f"Pobednik je {pobednik}! Partija je zapisana.")
   
    # Resetuj skorove za novu partiju
    for k in st.session_state.podaci["skorovi"]:
        st.session_state.podaci["skorovi"][k] = 0
    time.sleep(3)
    st.rerun()

# --- PRIKAZ ISTORIJE SA DATUMOM ---
if st.session_state.istorija:
    st.markdown("## 📜 ISTORIJA PARTIJA")
    for p in reversed(st.session_state.istorija):
        with st.expander(f"📅 {p['datum']} - {p['igra']}"):
            st.markdown(f"""
            <div class='history-card'>
                <p>🏆 <b>Pobednik:</b> <span style='color:#00ff00'>{p['pobednik']}</span></p>
                <p>📊 <b>Konačni skor:</b> {p['detalji']}</p>
            </div>
            """, unsafe_allow_html=True)

# SIDEBAR (MENI SA STRANE)
with st.sidebar:
    st.header("⚙️ Kontrole")
    if st.button("🏠 Početni ekran"):
        st.session_state.clear()
        st.rerun()
    st.write("---")
    st.write(f"Trenutna igra: **{st.session_state.igra_odabrana}**")