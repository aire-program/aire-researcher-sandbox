import streamlit as st
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.layout import render_header, render_sidebar
from app.config import PIPELINES_DIR

st.set_page_config(page_title="Pipeline Gallery | AIRE Sandbox", page_icon="🚀", layout="wide")

render_sidebar()
render_header()

st.title("Pipeline Gallery")
st.markdown("Explore the available Jupyter notebooks for AI-enabled research workflows.")

categories = {
    "Text Analysis": "text",
    "Tabular Data": "tabular",
    "RAG & Retrieval": "rag",
    "Prototypes": "prototypes"
}

for category_name, folder_name in categories.items():
    st.subheader(category_name)
    folder_path = os.path.join(PIPELINES_DIR, folder_name)
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if f.endswith('.ipynb')]
        if files:
            for f in files:
                st.markdown(f"- **{f}**: [Open in GitHub](../tree/main/pipelines/{folder_name}/{f})")
        else:
            st.info("No notebooks found in this category.")
    else:
        st.warning(f"Directory {folder_name} not found.")
