import streamlit as st
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.layout import render_header, render_sidebar

st.set_page_config(page_title="Governance | AIRE Sandbox", page_icon="⚖️", layout="wide")

render_sidebar()
render_header()

st.title("Governance & Safety")

GOV_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'governance'))

tab1, tab2 = st.tabs(["Responsible Use Guidelines", "Release Checklist"])

with tab1:
    path = os.path.join(GOV_DIR, 'responsible_use_guidelines.md')
    if os.path.exists(path):
        with open(path, 'r') as f:
            st.markdown(f.read())
    else:
        st.warning("Guidelines file not found.")

with tab2:
    path = os.path.join(GOV_DIR, 'review_before_release_checklist.md')
    if os.path.exists(path):
        with open(path, 'r') as f:
            st.markdown(f.read())
    else:
        st.warning("Checklist file not found.")
