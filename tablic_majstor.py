import streamlit as st

# Postavke ekrana
st.set_page_config(page_title="TAPI MAJSTOR v2.0", layout="wide")

# PROFESIONALNI STIL (Crna tema, ogromna dugmad, bela slova)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    h1, h2, h3 { color: #FFFFFF !important; text-align: center; }
    .stButton>button {
        width: 100%; height: 80px; font-size: 25px !important;
        background-color: #1A1A1A; color: white; border: 2px solid #4F8BF9; border-radius: 15px;
    }
    .total-box {
        font-size: 40px; font-weight: bold; text-align: center;
        background-color: #0E1117; padding: 15px; border: 3px solid #00FF00; border-radius: 20px;
    }
    input { font-size: 25px !important; }
    </style>
    """, unsafe_allow_html=True)

# NAVIGACIJA
if 'strana' not in st.session_state: st.session_state.strana = 'pocetna'
if 'remi_skor' not in st.session_state: st.session_state.remi_skor = {"Igrač 1": 0, "Igrač 2": 0, "Igrač 3": 0, "Igrač 4": 0}

# --- POČETNI EKRAN ---
if st.session_state.strana == 'pocetna':
    st.title("🏆 TAPI MAJSTOR")
    st.write("---")
    if st.button("🃏 IGRAJ TABLIĆ (6 PARTIJA)"):
        st.session_state.strana = 'tablic'
        st.rerun()
    st.write("")
    if st.button("🎴 IGRAJ REMI (PROFESIONALNO)"):
        st.session_state.strana = 'remi'
        st.rerun()

# --- REMI MODUL (ZA RODITELJE) ---
elif st.session_state.strana == 'remi':
    st.title("🎴 REMI ZAPISNIK")
    if st.button("⬅️ NAZAD U MENI"):
        st.session_state.strana = 'pocetna'
        st.rerun()

    # Prikaz trenutnog stanja (Veliki brojevi)
    cols = st.columns(4)
    for i, (igrac, poeni) in enumerate(st.session_state.remi_skor.items()):
        with cols[i]:
            st.markdown(f"### {igrac}")
            st.markdown(f'<div class="total-box">{poeni}</div>', unsafe_allow_html=True)
           
            # Unos za novu ruku
            nova_ruka = st.number_input(f"Dodaj", key=f"input_{igrac}", step=1)
           
            col_plus, col_minus = st.columns(2)
            with col_plus:
                if st.button(f"➕", key=f"p_{igrac}"):
                    st.session_state.remi_skor[igrac] += nova_ruka
                    st.rerun()
            with col_minus:
                if st.button(f"➖", key=f"m_{igrac}"):
                    st.session_state.remi_skor[igrac] -= nova_ruka
                    st.rerun()
           
            if st.button(f"KAZNA 100", key=f"k_{igrac}"):
                st.session_state.remi_skor[igrac] += 100
                st.rerun()

    if st.button("🔄 RESETUJ CELI REMI"):
        st.session_state.remi_skor = {k: 0 for k in st.session_state.remi_skor}
        st.rerun()

# --- TABLIĆ MODUL (TVOJ TURNIR) ---
elif st.session_state.strana == 'tablic':
    st.title("🃏 TABLIĆ TURNIR")
    # Ovde ide onaj tvoj kod za 6 partija koji smo malopre napravili...
    if st.button("⬅️ NAZAD"):
        st.session_state.strana = 'pocetna'
        st.rerun()
