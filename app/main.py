import streamlit as st
import sys
import os

# Add project root to sys.path to allow imports from app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.layout import render_header, render_sidebar

st.set_page_config(
    page_title="AIRE Sandbox",
    page_icon="🔬",
    layout="wide"
)

def main():
    render_sidebar()
    render_header()

    st.markdown("""
    ### Welcome to the AI Researcher Developer Sandbox
    
    This application serves as a browser and interface for the synthetic data and workflows 
    contained in this repository.
    
    **Get Started:**
    - **Overview**: See statistics about the synthetic dataset.
    - **Pipeline Gallery**: Explore available Jupyter notebooks.
    - **RAG Workbench**: Test retrieval-augmented generation patterns.
    - **API Tools**: Interact with the mock API clients.
    - **Governance**: Review safety checklists and guidelines.
    
    Please use the sidebar navigation to explore the different modules.
    """)

if __name__ == "__main__":
    main()
