import streamlit as st
import datetime

# 1. OSNOVNA PODEŠAVANJA
st.set_page_config(page_title="TAPI MAJSTOR PRO", layout="wide")

# 2. DIZAJN (BELA SLOVA, CRNA POZADINA, JASNE CRTE)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
   
    /* Glavna dugmad - BELA SLOVA MORAJU BITI BELA */
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
        margin-top: 35px;
        margin-bottom: 35px;
    }

    /* Kartice u istoriji */
    .istorija-card {
        background: #111111; padding: 20px; border-left: 8px solid #4F8BF9;
        margin-bottom: 15px; border-radius: 10px; color: #FFFFFF; font-size: 20px;
    }

    h1, h2, h3, p, label { color: white !important; text-align: center; }
    input { background-color: #222222 !important; color: white !important; font-size: 20px !important; }
   
    .stRadio label { color: white !important; font-size: 22px !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. MASIVNA INICIJALIZACIJA (Sve opcije spremne unapred)
if 'strana' not in st.session_state: st.session_state.strana = 'pocetna'
if 'istorija_tablic' not in st.session_state: st.session_state.istorija_tablic = []
if 'istorija_remi' not in st.session_state: st.session_state.istorija_remi = []
if 'imena' not in st.session_state: st.session_state.imena = ["Igrač 1", "Igrač 2", "Igrač 3", "Igrač 4"]
if 'ime_g_a' not in st.session_state: st.session_state.ime_g_a = "Grupa A"
if 'ime_g_b' not in st.session_state: st.session_state.ime_g_b = "Grupa B"

# Rezervacija memorije za svakog mogućeg aktera (Igrači + Grupe)
svi_akteri = ["Igrač 1", "Igrač 2", "Igrač 3", "Igrač 4", "Grupa A", "Grupa B"]

# Inicijalizacija poena za Tablić
if 't_bodovi' not in st.session_state:
    st.session_state.t_bodovi = {ime: {1:0, 2:0, 3:0, 4:0, 5:0, 6:0} for ime in svi_akteri}
    st.session_state.t_recke = {ime: {1:0, 2:0, 3:0, 4:0, 5:0, 6:0} for ime in svi_akteri}

# Inicijalizacija poena za Remi
if 'r_bodovi' not in st.session_state:
    st.session_state.r_bodovi = {ime: 0 for ime in svi_akteri}

def promeni_stranu(nova):
    st.session_state.strana = nova
    st.rerun()

# --- EKRAN 1: POCETNI MENI ---
if st.session_state.strana == 'pocetna':
    st.markdown("<h1 style='font-size: 60px;'>🏆 TAPI MAJSTOR</h1>", unsafe_allow_html=True)
    if st.button("🎮 NOVA IGRA"): promeni_stranu('biraj_igru')
    if st.button("📊 PREGLED REZULTATA"): promeni_stranu('biraj_pregled')
   
    st.write("---")
    with st.expander("⚙️ PODESI IMENA ZA IGRAČE ILI GRUPE"):
        st.session_state.imena[0] = st.text_input("Ime Igrača 1:", st.session_state.imena[0], key="set_i1")
        st.session_state.imena[1] = st.text_input("Ime Igrača 2:", st.session_state.imena[1], key="set_i2")
        st.session_state.imena[2] = st.text_input("Ime Igrača 3:", st.session_state.imena[2], key="set_i3")
        st.session_state.imena[3] = st.text_input("Ime Igrača 4:", st.session_state.imena[3], key="set_i4")
        st.write("---")
        # Ovde unosiš imena za tvoju opciju sa grupama
        novi_a = st.text_input("Ime PRVE GRUPE:", st.session_state.ime_g_a, key="set_ga")
        novi_b = st.text_input("Ime DRUGE GRUPE:", st.session_state.ime_g_b, key="set_gb")
       
        # Ažuriranje memorije ako se imena grupa promene
        if novi_a != st.session_state.ime_g_a:
            st.session_state.t_bodovi[novi_a] = st.session_state.t_bodovi.pop(st.session_state.ime_g_a, {1:0,2:0,3:0,4:0,5:0,6:0})
            st.session_state.t_recke[novi_a] = st.session_state.t_recke.pop(st.session_state.ime_g_a, {1:0,2:0,3:0,4:0,5:0,6:0})
            st.session_state.r_bodovi[novi_a] = st.session_state.r_bodovi.pop(st.session_state.ime_g_a, 0)
            st.session_state.ime_g_a = novi_a
        if novi_b != st.session_state.ime_g_b:
            st.session_state.t_bodovi[novi_b] = st.session_state.t_bodovi.pop(st.session_state.ime_g_b, {1:0,2:0,3:0,4:0,5:0,6:0})
            st.session_state.t_recke[novi_b] = st.session_state.t_recke.pop(st.session_state.ime_g_b, {1:0,2:0,3:0,4:0,5:0,6:0})
            st.session_state.r_bodovi[novi_b] = st.session_state.r_bodovi.pop(st.session_state.ime_g_b, 0)
            st.session_state.ime_g_b = novi_b

# --- EKRAN 2: IZBOR IGRE ---
elif st.session_state.strana == 'biraj_igru':
    st.title("ŠTA IGRAMO?")
    if st.button("🃏 TABLIĆ"): promeni_stranu('igra_tablic')
    if st.button("🎴 REMI"): promeni_stranu('igra_remi')
    if st.button("⬅️ NAZAD"): promeni_stranu('pocetna')

# --- EKRAN 3: IZBOR PREGLEDA ---
elif st.session_state.strana == 'biraj_pregled':
    st.title("IZABERI ISTORIJU")
    if st.button("📜 TABLIĆ ISTORIJA"): promeni_stranu('vidi_tablic')
    if st.button("📜 REMI ISTORIJA"): promeni_stranu('vidi_remi')
    if st.button("⬅️ NAZAD"): promeni_stranu('pocetna')

# --- EKRAN 4: TABLIĆ (BEZ SKRAĆIVANJA) ---
elif st.session_state.strana == 'igra_tablic':
    st.title("🃏 TABLIĆ (6 PARTIJA)")
    mod_t = st.radio("Ko igra?", ["2 Igrača", "4 Igrača", "2 Grupe"], horizontal=True, key="radio_t")
   
    if mod_t == "2 Igrača": ucesnici = [st.session_state.imena[0], st.session_state.imena[1]]
    elif mod_t == "2 Grupe": ucesnici = [st.session_state.ime_g_a, st.session_state.ime_g_b]
    else: ucesnici = st.session_state.imena

    # Pisanje svake partije posebno za stabilnost
    for p in [1, 2, 3, 4, 5, 6]:
        st.markdown(f"## 🏁 PARTIJA {p}")
        kol = st.columns(len(ucesnici))
        for i, ime in enumerate(ucesnici):
            with kol[i]:
                st.write(f"**{ime}**")
                # Unos poena
                st.session_state.t_bodovi[ime][p] = st.number_input(f"Bodovi {p}-{ime}", 0, 30, key=f"in_t_{p}_{ime}", label_visibility="collapsed")
                # Recke
                trenutni_r = st.session_state.t_recke[ime][p]
                if st.button(f"➕ RECKA ({trenutni_r})", key=f"btn_t_{p}_{ime}"):
                    st.session_state.t_recke[ime][p] += 1
                    st.rerun()
        # DEBELA CRTA IZMEĐU PARTIJA
        if p < 6:
            st.markdown('<div class="partija-crta"></div>', unsafe_allow_html=True)

    st.divider()
    zbir_kol = st.columns(len(ucesnici))
    zapis_t = f"{datetime.datetime.now().strftime('%H:%M')} | "
    for i, ime in enumerate(ucesnici):
        ukupno = sum(st.session_state.t_bodovi[ime].values()) + sum(st.session_state.t_recke[ime].values())
        with zbir_kol[i]:
            st.markdown(f"**{ime} UKUPNO:**")
            st.markdown(f'<div class="total-box">{ukupno}</div>', unsafe_allow_html=True)
            zapis_t += f"{ime}: {ukupno} "

    if st.button("💾 SAČUVAJ"):
        st.session_state.istorija_tablic.append(zapis_t)
        st.success("Upisano!")
    if st.button("⬅️ NAZAD"): promeni_stranu('biraj_igru')

# --- EKRAN 5: REMI (BELA SLOVA I KAZNE) ---
elif st.session_state.strana == 'igra_remi':
    st.title("🎴 REMI ZAPISNIK")
    mod_r = st.radio("Ko igra?", ["2 Igrača", "4 Igrača", "2 Grupe"], horizontal=True, key="radio_r")
   
    if mod_r == "2 Igrača": ucesnici_r = [st.session_state.imena[0], st.session_state.imena[1]]
    elif mod_r == "2 Grupe": ucesnici_r = [st.session_state.ime_g_a, st.session_state.ime_g_b]
    else: ucesnici_r = st.session_state.imena

    kol_r = st.columns(len(ucesnici_r))
    for i, ime in enumerate(ucesnici_r):
        with kol_r[i]:
            st.markdown(f"### {ime}")
            st.markdown(f'<div class="total-box">{st.session_state.r_bodovi[ime]}</div>', unsafe_allow_html=True)
            un_r = st.number_input("Poeni:", 0, 500, key=f"in_r_{ime}")
           
            c1, c2 = st.columns(2)
            if c1.button("➕ DODAJ", key=f"btn_r_p_{ime}"):
                st.session_state.r_bodovi[ime] += un_r
                st.rerun()
            if c2.button("➖ SKINI", key=f"btn_r_m_{ime}"):
                st.session_state.r_bodovi[ime] -= un_r
                st.rerun()
            if st.button("⚠️ KAZNA 100", key=f"btn_r_k_{ime}"):
                st.session_state.r_bodovi[ime] += 100
                st.rerun()

    if st.button("💾 SAČUVAJ"):
        zapis_r = f"{datetime.datetime.now().strftime('%H:%M')} | {mod_r} | "
        for a in ucesnici_r: zapis_r += f"{a}: {st.session_state.r_bodovi[a]} "
        st.session_state.istorija_remi.append(zapis_r)
        st.success("Sačuvano!")
    if st.button("⬅️ NAZAD"): promeni_stranu('biraj_igru')

# --- EKRAN 6: PRIKAZ ISTORIJE ---
elif st.session_state.strana == 'vidi_tablic':
    st.title("📜 ISTORIJA TABLIĆA")
    for s in reversed(st.session_state.istorija_tablic): st.markdown(f'<div class="istorija-card">{s}</div>', unsafe_allow_html=True)
    if st.button("⬅️ NAZAD"): promeni_stranu('biraj_pregled')

elif st.session_state.strana == 'vidi_remi':
    st.title("📜 ISTORIJA REMIJA")
    for s in reversed(st.session_state.istorija_remi): st.markdown(f'<div class="istorija-card">{s}</div>', unsafe_allow_html=True)
    if st.button("⬅️ NAZAD"): promeni_stranu('biraj_pregled')
