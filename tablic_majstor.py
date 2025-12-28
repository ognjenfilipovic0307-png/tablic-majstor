import streamlit as st
import datetime

# 1. PODEŠAVANJE STRANICE
st.set_page_config(page_title="TAPI MAJSTOR PRO", layout="wide")

# 2. DIZAJN (Sve je na crnom, bela slova, ogromna dugmad)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    .stButton>button {
        width: 100%; height: 75px; font-size: 22px !important;
        background-color: #1A1A1A; color: white; border: 2px solid #4F8BF9; border-radius: 12px;
    }
    .total-box {
        font-size: 35px; font-weight: bold; text-align: center;
        color: #00FF00; background: #111; padding: 15px; border-radius: 15px; border: 2px solid #333;
    }
    .istorija-card { background: #111; padding: 15px; border-left: 5px solid #4F8BF9; margin-bottom: 10px; border-radius: 5px; }
    h1, h2, h3 { text-align: center; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. INICIJALIZACIJA (Ovo čuva aplikaciju od pucanja)
if 'strana' not in st.session_state: st.session_state.strana = 'pocetna'
if 'istorija_tablic' not in st.session_state: st.session_state.istorija_tablic = []
if 'istorija_remi' not in st.session_state: st.session_state.istorija_remi = []
if 'imena' not in st.session_state: st.session_state.imena = ["Igrač 1", "Igrač 2", "Igrač 3", "Igrač 4"]

# Inicijalizacija poena za Tablić (6 partija za svaku moguću kombinaciju)
if 't_skor' not in st.session_state:
    svi_akteri = ["Grupa A", "Grupa B", "Igrač 1", "Igrač 2", "Igrač 3", "Igrač 4"]
    st.session_state.t_skor = {a: {"p": [0]*7, "r": [0]*7} for a in svi_akteri}

# Inicijalizacija za Remi
if 'r_skor' not in st.session_state:
    svi_akteri = ["Grupa A", "Grupa B", "Igrač 1", "Igrač 2", "Igrač 3", "Igrač 4"]
    st.session_state.r_skor = {a: 0 for a in svi_akteri}

def idi_na(nova_strana):
    st.session_state.strana = nova_strana
    st.rerun()

# --- EKRAN 1: POČETNI MENI ---
if st.session_state.strana == 'pocetna':
    st.title("🏆 TAPI MAJSTOR")
    if st.button("🎮 IGRAJ"):
        idi_na('izbor_igre')
    if st.button("📊 PREGLED TABELE"):
        idi_na('izbor_pregleda')
   
    with st.expander("⚙️ PODESI IMENA IGRAČA"):
        for i in range(4):
            st.session_state.imena[i] = st.text_input(f"Ime za igrača {i+1}:", st.session_state.imena[i], key=f"ime_{i}")

# --- EKRAN 2: IZBOR IGRE ---
elif st.session_state.strana == 'izbor_igre':
    st.title("IZABERI IGRU")
    if st.button("🃏 TABLIĆ"):
        idi_na('igra_tablic')
    if st.button("🎴 REMI"):
        idi_na('igra_remi')
    if st.button("⬅️ NAZAD NA POČETAK"):
        idi_na('pocetna')

# --- EKRAN 3: IZBOR PREGLEDA ---
elif st.session_state.strana == 'izbor_pregleda':
    st.title("PREGLED REZULTATA")
    if st.button("📜 ISTORIJA TABLIĆA"):
        idi_na('pregled_tablic')
    if st.button("📜 ISTORIJA REMIJA"):
        idi_na('pregled_remi')
    if st.button("⬅️ NAZAD NA POČETAK"):
        idi_na('pocetna')

# --- EKRAN 4: TABLIĆ (6 PARTIJA + GRUPE) ---
elif st.session_state.strana == 'igra_tablic':
    st.title("🃏 TABLIĆ (6 PARTIJA)")
    mod = st.radio("Izaberi format:", ["4 Igrača", "2 Grupe"], horizontal=True)
    akteri = ["Grupa A", "Grupa B"] if mod == "2 Grupe" else st.session_state.imena
   
    # Prikaz 6 partija
    for p in range(1, 7):
        st.markdown(f"### 🏁 PARTIJA {p}")
        cols = st.columns(len(akteri))
        for idx, a in enumerate(akteri):
            with cols[idx]:
                st.write(f"**{a}**")
                # Unos poena (0-30)
                st.session_state.t_skor[a]["p"][p] = st.number_input(f"Poeni {a} P{p}", 0, 30, key=f"tp_{a}_{p}", label_visibility="collapsed")
                # Dugme za recku
                if st.button(f"➕ Recka ({st.session_state.t_skor[a]['r'][p]})", key=f"tr_{a}_{p}"):
                    st.session_state.t_skor[a]["r"][p] += 1
                    st.rerun()
   
    st.divider()
    # Ukupan zbir na dnu
    res_cols = st.columns(len(akteri))
    vreme = datetime.datetime.now().strftime('%H:%M')
    zapis = f"{vreme} | "
   
    for i, a in enumerate(akteri):
        ukupno = sum(st.session_state.t_skor[a]["p"]) + sum(st.session_state.t_skor[a]["r"])
        res_cols[i].markdown(f"**{a} UKUPNO:**")
        res_cols[i].markdown(f'<div class="total-box">{ukupno}</div>', unsafe_allow_html=True)
        zapis += f"{a}: {ukupno} "

    if st.button("💾 ZAVRŠI I SAČUVAJ"):
        st.session_state.istorija_tablic.append(zapis)
        st.success("Rezultat je sačuvan u tabelu!")
   
    if st.button("⬅️ NAZAD"):
        idi_na('izbor_igre')

# --- EKRAN 5: REMI (KAZNE + GRUPE) ---
elif st.session_state.strana == 'igra_remi':
    st.title("🎴 REMI ZAPISNIK")
    mod_r = st.radio("Format igre:", ["4 Igrača", "2 Grupe"], horizontal=True)
    akteri_r = ["Grupa A", "Grupa B"] if mod_r == "2 Grupe" else st.session_state.imena
   
    cols_r = st.columns(len(akteri_r))
    for i, a in enumerate(akteri_r):
        with cols_r[i]:
            st.markdown(f"### {a}")
            st.markdown(f'<div class="total-box">{st.session_state.r_skor[a]}</div>', unsafe_allow_html=True)
            unos = st.number_input("Unesi poene:", 0, 500, key=f"runos_{a}")
           
            c1, c2 = st.columns(2)
            if c1.button("➕ DODAJ", key=f"rplus_{a}"):
                st.session_state.r_skor[a] += unos
                st.rerun()
            if c2.button("➖ ODUZMI", key=f"rminus_{a}"):
                st.session_state.r_skor[a] -= unos
                st.rerun()
           
            if st.button("⚠️ KAZNA 100", key=f"rkazna_{a}"):
                st.session_state.r_skor[a] += 100
                st.rerun()

    st.divider()
    if st.button("💾 SAČUVAJ KRAJNJI REZULTAT"):
        vreme_r = datetime.datetime.now().strftime('%H:%M')
        zapis_r = f"{vreme_r} | "
        for a in akteri_r:
            zapis_r += f"{a}: {st.session_state.r_skor[a]} "
        st.session_state.istorija_remi.append(zapis_r)
        st.success("Sačuvano!")

    if st.button("⬅️ NAZAD"):
        idi_na('izbor_igre')

# --- EKRAN 6: PRIKAZ ISTORIJE ---
elif st.session_state.strana == 'pregled_tablic':
    st.title("📜 ISTORIJA: TABLIĆ")
    if not st.session_state.istorija_tablic:
        st.write("Nema sačuvanih rezultata.")
    for stavka in reversed(st.session_state.istorija_tablic):
        st.markdown(f'<div class="istorija-card">{stavka}</div>', unsafe_allow_html=True)
    if st.button("⬅️ NAZAD"):
        idi_na('izbor_pregleda')

elif st.session_state.strana == 'pregled_remi':
    st.title("📜 ISTORIJA: REMI")
    if not st.session_state.istorija_remi:
        st.write("Nema sačuvanih rezultata.")
    for stavka in reversed(st.session_state.istorija_remi):
        st.markdown(f'<div class="istorija-card">{stavka}</div>', unsafe_allow_html=True)
    if st.button("⬅️ NAZAD"):
        idi_na('izbor_pregleda')


