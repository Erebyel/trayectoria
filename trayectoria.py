import streamlit as st
from streamlit_timeline import timeline
st.set_page_config(page_title="Timeline Example", layout="wide", initial_sidebar_state = 'expanded')
with open('trayectoria.json', "r") as f:
    data = f.read()
timeline(data, height=650)
