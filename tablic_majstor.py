import streamlit as st
import datetime

# 1. OSNOVNA PODEŠAVANJA STRANICE
st.set_page_config(page_title="TAPI MAJSTOR PRO", layout="wide")

# 2. KOMPLETAN DIZAJN (CSS)
# Ovde smo osigurali da su slova na glavnim dugmićima BELA
st.markdown("""
    <style>
    /* Pozadina cele aplikacije */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
   
    /* Glavna dugmad (IGRAJ, PREGLED STATISTIKE, itd.) */
    .stButton>button {
        width: 100%;
        height: 75px;
        font-size: 24px !important;
        background-color: #1A1A1A;
        color: #FFFFFF !important;
        border: 2px solid #4F8BF9;
        border-radius: 12px;
        font-weight: bold;
        display: block;
    }
   
    /* Efekat kada se pređe mišem preko dugmeta */
    .stButton>button:hover {
        border-color: #00FF00;
        color: #00FF00 !important;
    }

    /* Kutija za ukupan rezultat (Zeleni brojevi) */
    .total-box {
        font-size: 38px;
        font-weight: bold;
        text-align: center;
        color: #00FF00;
        background: #111111;
        padding: 15px;
        border-radius: 15px;
        border: 2px solid #333333;
        margin-top: 10px;
    }

    /* Kartice u istoriji rezultata */
    .istorija-card {
        background: #111111;
        padding: 15px;
        border-left: 6px solid #4F8BF9;
        margin-bottom: 12px;
        border-radius: 8px;
        color: #FFFFFF;
        font-size: 18px;
    }

    /* Podešavanje boja za tekstove, naslove i label-e */
    h1, h2, h3, p, label, .stMarkdown {
        color: white !important;
        text-align: center;
    }
   
    /* Posebno za radio dugmiće (izbor formata) */
    .stRadio label {
        color: white !important;
        font-size: 20px !important;
    }
   
    /* Boja unosa brojeva */
    input {
        background-color: #222222 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. INICIJALIZACIJA MEMORIJE (Session State)
# Ovo sprečava da se aplikacija sruši kada se osveži strana
if 'strana' not in st.session_state:
    st.session_state.strana = 'pocetna'

if 'istorija_tablic' not in st.session_state:
    st.session_state.istorija_tablic = []

if 'istorija_remi' not in st.session_state:
    st.session_state.istorija_remi = []

if 'imena' not in st.session_state:
    st.session_state.imena = ["Igrač 1", "Igrač 2", "Igrač 3", "Igrač 4"]

# Inicijalizacija baze poena za Tablić (svih 6 partija)
if 't_skor' not in st.session_state:
    akteri = ["Grupa A", "Grupa B", "Igrač 1", "Igrač 2", "Igrač 3", "Igrač 4"]
    st.session_state.t_skor = {a: {"p": [0]*7, "r": [0]*7} for a in akteri}

# Inicijalizacija baze poena za Remi
if 'r_skor' not in st.session_state:
    akteri = ["Grupa A", "Grupa B", "Igrač 1", "Igrač 2", "Igrač 3", "Igrač 4"]
    st.session_state.r_skor = {a: 0 for a in akteri}

# Funkcija za laku navigaciju kroz aplikaciju
def promeni_ekran(ime_strane):
    st.session_state.strana = ime_strane
    st.rerun()

# --- EKRAN 1: GLAVNI POČETNI MENI ---
if st.session_state.strana == 'pocetna':
    st.markdown("<h1 style='font-size: 50px;'>🏆 TAPI MAJSTOR</h1>", unsafe_allow_html=True)
    st.write("Dobrodošli! Izaberite opciju:")
   
    if st.button("🎮 IGRAJ"):
        promeni_ekran('izbor_igre')
       
    if st.button("📊 PREGLED STATISTIKE"):
        promeni_ekran('izbor_pregleda')
   
    st.divider()
    with st.expander("⚙️ PODESI IMENA IGRAČA (Opciono)"):
        for i in range(4):
            st.session_state.imena[i] = st.text_input(f"Ime za igrača {i+1}:", st.session_state.imena[i], key=f"set_ime_{i}")

# --- EKRAN 2: IZBOR IGRE (TABLIĆ ILI REMI) ---
elif st.session_state.strana == 'izbor_igre':
    st.title("Šta igramo danas?")
   
    if st.button("🃏 IGRAJ TABLIĆ"):
        promeni_ekran('igra_tablic')
       
    if st.button("🎴 IGRAJ REMI"):
        promeni_ekran('igra_remi')
       
    if st.button("⬅️ NAZAD NA POČETAK"):
        promeni_ekran('pocetna')

# --- EKRAN 3: IZBOR PREGLEDA (ISTORIJA) ---
elif st.session_state.strana == 'izbor_pregleda':
    st.title("Pregled sačuvanih rezultata")
   
    if st.button("📜 ISTORIJA TABLIĆA"):
        promeni_ekran('prikaz_tablic')
       
    if st.button("📜 ISTORIJA REMIJA"):
        promeni_ekran('prikaz_remi')
       
    if st.button("⬅️ NAZAD NA POČETAK"):
        promeni_ekran('pocetna')

# --- EKRAN 4: LOGIKA ZA TABLIĆ (6 PARTIJA) ---
elif st.session_state.strana == 'igra_tablic':
    st.title("🃏 TABLIĆ: TURNIR OD 6 PARTIJA")
   
    izbor_formata = st.radio("Izaberi format:", ["4 Igrača", "2 Grupe"], horizontal=True, key="tablic_format")
    akteri_t = ["Grupa A", "Grupa B"] if izbor_formata == "2 Grupe" else st.session_state.imena
   
    # Tabela sa unosa poena za svih 6 partija
    for partija_br in range(1, 7):
        st.markdown(f"### PARTIJA {partija_br}")
        kolone = st.columns(len(akteri_t))
       
        for idx, ime_akter in enumerate(akteri_t):
            with kolone[idx]:
                st.write(f"**{ime_akter}**")
                # Unos osnovnih bodova
                st.session_state.t_skor[ime_akter]["p"][partija_br] = st.number_input(
                    f"Bodovi {ime_akter} P{partija_br}", 0, 30,
                    key=f"input_p_{ime_akter}_{partija_br}", label_visibility="collapsed"
                )
                # Dugme za recke (špileve)
                if st.button(f"➕ Recka ({st.session_state.t_skor[ime_akter]['r'][partija_br]})", key=f"recka_{ime_akter}_{partija_br}"):
                    st.session_state.t_skor[ime_akter]["r"][partija_br] += 1
                    st.rerun()
   
    st.divider()
   
    # Prikaz ukupnog rezultata na dnu
    rez_kolone = st.columns(len(akteri_t))
    trenutno_vreme = datetime.datetime.now().strftime('%d.%m. u %H:%M')
    tekst_za_istoriju = f"{trenutno_vreme} | "
   
    for i, ime_akter in enumerate(akteri_t):
        zbir_poena = sum(st.session_state.t_skor[ime_akter]["p"]) + sum(st.session_state.t_skor[ime_akter]["r"])
        rez_kolone[i].markdown(f"**{ime_akter} UKUPNO:**")
        rez_kolone[i].markdown(f'<div class="total-box">{zbir_poena}</div>', unsafe_allow_html=True)
        tekst_za_istoriju += f"{ime_akter}: {zbir_poena} "

    # Dugme za čuvanje u bazu
    if st.button("💾 SAČUVAJ OVU PARTIJU U ISTORIJU"):
        st.session_state.istorija_tablic.append(tekst_za_istoriju)
        st.success("Rezultat je uspešno upisan!")
       
    if st.button("⬅️ NAZAD"):
        promeni_ekran('izbor_igre')

# --- EKRAN 5: LOGIKA ZA REMI ---
elif st.session_state.strana == 'igra_remi':
    st.title("🎴 REMI: PROFESIONALNI ZAPISNIK")
   
    izbor_formata_r = st.radio("Format igre:", ["4 Igrača", "2 Grupe"], horizontal=True, key="remi_format")
    akteri_r = ["Grupa A", "Grupa B"] if izbor_formata_r == "2 Grupe" else st.session_state.imena
   
    kolone_r = st.columns(len(akteri_r))
   
    for i, ime_akter in enumerate(akteri_r):
        with kolone_r[i]:
            st.markdown(f"### {ime_akter}")
            # Prikaz trenutnog stanja
            st.markdown(f'<div class="total-box">{st.session_state.r_skor.get(ime_akter, 0)}</div>', unsafe_allow_html=True)
           
            unos_remi = st.number_input("Unesi broj poena:", 0, 500, key=f"remi_unos_{ime_akter}")
           
            c1, c2 = st.columns(2)
            if c1.button("➕ DODAJ", key=f"r_plus_{ime_akter}"):
                st.session_state.r_skor[ime_akter] += unos_remi
                st.rerun()
            if c2.button("➖ ODUZMI", key=f"r_minus_{ime_akter}"):
                st.session_state.r_skor[ime_akter] -= unos_remi
                st.rerun()
           
            # Dugme za kaznu 100
            if st.button("⚠️ KAZNA 100", key=f"r_kazna_{ime_akter}"):
                st.session_state.r_skor[ime_akter] += 100
                st.rerun()

    st.divider()
   
    if st.button("💾 SAČUVAJ KRAJNJI REZULTAT REMIJA"):
        vreme_r = datetime.datetime.now().strftime('%d.%m. u %H:%M')
        zapis_remi = f"{vreme_r} | "
        for a in akteri_r:
            zapis_remi += f"{a}: {st.session_state.r_skor[a]} "
        st.session_state.istorija_remi.append(zapis_remi)
        st.success("Rezultat sačuvan!")
       
    if st.button("⬅️ NAZAD"):
        promeni_ekran('izbor_igre')

# --- EKRAN 6: PRIKAZ ISTORIJE REZULTATA ---
elif st.session_state.strana == 'prikaz_tablic':
    st.title("📜 ISTORIJA PARTIJA: TABLIĆ")
    if not st.session_state.istorija_tablic:
        st.write("Još uvek nema sačuvanih partija Tablića.")
    else:
        for stavka in reversed(st.session_state.istorija_tablic):
            st.markdown(f'<div class="istorija-card">{stavka}</div>', unsafe_allow_html=True)
   
    if st.button("🗑️ OBRIŠI CELU ISTORIJU TABLIĆA"):
        st.session_state.istorija_tablic = []
        st.rerun()
   
    if st.button("⬅️ NAZAD NA PREGLED"):
        promeni_ekran('izbor_pregleda')

elif st.session_state.strana == 'prikaz_remi':
    st.title("📜 ISTORIJA PARTIJA: REMI")
    if not st.session_state.istorija_remi:
        st.write("Još uvek nema sačuvanih partija Remija.")
    else:
        for stavka in reversed(st.session_state.istorija_remi):
            st.markdown(f'<div class="istorija-card">{stavka}</div>', unsafe_allow_html=True)
           
    if st.button("🗑️ OBRIŠI CELU ISTORIJU REMIJA"):
        st.session_state.istorija_remi = []
        st.rerun()
       
    if st.button("⬅️ NAZAD NA PREGLED"):
        promeni_ekran('izbor_pregleda')
