import streamlit as st
import numpy as np
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.layout import render_header, render_sidebar

st.set_page_config(page_title="API Tools | AIRE Sandbox", page_icon="🔌", layout="wide")

render_sidebar()
render_header()

st.title("API Tools")
st.markdown("Demonstration of the mock API clients included in `api/python/`.")

tab1, tab2 = st.tabs(["REST Client", "Embeddings Client"])

with tab1:
    st.subheader("REST API Client Simulator")
    st.markdown("Simulates fetching data from an external research API.")
    
    if st.button("Fetch Mock Data"):
        # Simulate client behavior inline for demo
        data = {
            "status": "success",
            "data": [
                {"id": 1, "name": "Project Alpha", "status": "active"},
                {"id": 2, "name": "Project Beta", "status": "completed"}
            ]
        }
        st.json(data)

with tab2:
    st.subheader("Embeddings Client Simulator")
    st.markdown("Simulates generating vector embeddings for text.")
    
    text_input = st.text_area("Enter text to embed:", "The quick brown fox jumps over the lazy dog.")
    
    if st.button("Generate Embedding"):
        # Simulate embedding
        embedding = np.random.rand(1, 768)
        st.write(f"Embedding shape: {embedding.shape}")
        st.write("First 10 dimensions:")
        st.code(str(embedding[0][:10]))
