# 1. PODEŠAVANJE STRANICE
st.set_page_config(page_title="TAPI MAJSTOR PRO", layout="wide")

# 2. DIZAJN (Sve je na crnom, bela slova, ogromna dugmad sa BELIM tekstom)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    /* Stil za dugmiće - slova su sada čisto BELA */
    .stButton>button {
        width: 100%; height: 75px; font-size: 24px !important;
        background-color: #1A1A1A; color: #FFFFFF !important;
        border: 2px solid #4F8BF9; border-radius: 12px;
        font-weight: bold;
    }
    .total-box {
        font-size: 35px; font-weight: bold; text-align: center;
        color: #00FF00; background: #111; padding: 15px; border-radius: 15px; border: 2px solid #333;
    }
    .istorija-card { background:

