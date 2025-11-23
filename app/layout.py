import streamlit as st

def render_header():
    st.markdown("## AI Researcher Developer Sandbox")
    st.markdown("**AIRE Program** – Applied AI Innovation & Research Enablement")
    st.markdown("---")

def render_sidebar():
    with st.sidebar:
        st.image("https://via.placeholder.com/150?text=AIRE+Sandbox", use_column_width=True)
        st.markdown("### Navigation")
        st.info("Select a page from the menu above.")
        st.markdown("---")
        st.markdown("### Resources")
        st.markdown("[GitHub Repo](https://github.com/YOUR_USERNAME/aire-researcher-sandbox)")
        st.markdown("[AIRE Program](https://socialscience.msu.edu)")
