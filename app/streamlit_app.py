import streamlit as st
from catppuccin import PALETTE

# ------------------------------------------------------------------------------
# THEME
# ------------------------------------------------------------------------------

mocha = PALETTE.mocha.colors

st.set_page_config(
    page_title="Title",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    f"""
    <style>
        :root {{
            --ctp-rosewater: {mocha.rosewater.hex};
            --ctp-flamingo: {mocha.flamingo.hex};
            --ctp-pink: {mocha.pink.hex};
            --ctp-mauve: {mocha.mauve.hex};
            --ctp-red: {mocha.red.hex};
            --ctp-maroon: {mocha.maroon.hex};
            --ctp-peach: {mocha.peach.hex};
            --ctp-yellow: {mocha.yellow.hex};
            --ctp-green: {mocha.green.hex};
            --ctp-teal: {mocha.teal.hex};
            --ctp-sky: {mocha.sky.hex};
            --ctp-sapphire: {mocha.sapphire.hex};
            --ctp-blue: {mocha.blue.hex};
            --ctp-lavender: {mocha.lavender.hex};

            --ctp-text: {mocha.text.hex};
            --ctp-subtext1: {mocha.subtext1.hex};
            --ctp-subtext0: {mocha.subtext0.hex};
            --ctp-overlay2: {mocha.overlay2.hex};
            --ctp-overlay1: {mocha.overlay1.hex};
            --ctp-overlay0: {mocha.overlay0.hex};
            --ctp-surface2: {mocha.surface2.hex};
            --ctp-surface1: {mocha.surface1.hex};
            --ctp-surface0: {mocha.surface0.hex};

            --ctp-base: {mocha.base.hex};
            --ctp-mantle: {mocha.mantle.hex};
            --ctp-crust: {mocha.crust.hex};
        }}

        .stApp {{
            background-color: var(--ctp-base);
            color: var(--ctp-text);
        }}

        section[data-testid="stSidebar"] {{
            background-color: var(--ctp-mantle);
            border-right: 1px solid var(--ctp-surface0);
        }}

        div[data-testid="stHeader"] {{
            background-color: var(--ctp-base);
            border-bottom: 1px solid var(--ctp-surface0);
        }}

        div[data-testid="stToolbar"] {{
            visibility: hidden;
            height: 0;
            position: fixed;
        }}

        .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
        }}

        h1, h2, h3, h4, h5, h6 {{
            color: var(--ctp-text);
        }}

        p, label, span, div {{
            color: var(--ctp-text);
        }}

        .stButton > button {{
            background-color: var(--ctp-mauve);
            color: var(--ctp-base);
            border: none;
            border-radius: 0.75rem;
        }}

        .stButton > button:hover {{
            background-color: var(--ctp-lavender);
            color: var(--ctp-base);
        }}

        .stTextInput > div > div > input,
        .stTextArea textarea {{
            background-color: var(--ctp-mantle);
            color: var(--ctp-text);
            border: 1px solid var(--ctp-surface0);
            border-radius: 0.75rem;
        }}

        .stSelectbox div[data-baseweb="select"] > div {{
            background-color: var(--ctp-mantle);
            color: var(--ctp-text);
            border: 1px solid var(--ctp-surface0);
            border-radius: 0.75rem;
        }}

        .stSlider div[data-baseweb="slider"] {{
            color: var(--ctp-mauve);
        }}

        div[data-testid="stMetric"] {{
            background-color: var(--ctp-mantle);
            border: 1px solid var(--ctp-surface0);
            padding: 1rem;
            border-radius: 1rem;
        }}

        div[data-testid="stCodeBlock"] {{
            border-radius: 1rem;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------------------
# APP
# ------------------------------------------------------------------------------

st.title("Title")
st.write("Description")