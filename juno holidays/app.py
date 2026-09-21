import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Juno Holidays — Travel Is For Everyone",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's default chrome so the travel website feels like a standalone site.
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        [data-testid="stToolbar"] {visibility: hidden; height: 0;}
        [data-testid="stDecoration"] {display: none;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        .stApp {background: #06111F;}
        iframe {border: none !important; width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_FILE = Path(__file__).with_name("juno-holidays.html")

if not HTML_FILE.exists():
    st.error("juno-holidays.html was not found next to app.py")
    st.stop()

html = HTML_FILE.read_text(encoding="utf-8")

# The original Claude-generated website is kept intact.
# Streamlit acts as the Python host while the original HTML/CSS/JS runs in the component.
components.html(
    html,
    height=5000,
    scrolling=True,
)
