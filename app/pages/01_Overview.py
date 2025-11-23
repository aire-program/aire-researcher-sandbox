import streamlit as st
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.layout import render_header, render_sidebar
from app.utils import load_articles, load_notes, load_experiments, load_metrics

st.set_page_config(page_title="Overview | AIRE Sandbox", page_icon="📊", layout="wide")

render_sidebar()
render_header()

st.title("Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

articles = load_articles()
notes = load_notes()
experiments = load_experiments()
metrics = load_metrics()

with col1:
    st.metric("Articles", len(articles))
with col2:
    st.metric("Field Notes", len(notes))
with col3:
    st.metric("Experiments", len(experiments))
with col4:
    st.metric("Metrics", len(metrics))

st.markdown("### Data Previews")

tab1, tab2, tab3, tab4 = st.tabs(["Articles", "Notes", "Experiments", "Metrics"])

with tab1:
    st.dataframe(articles.head(10), use_container_width=True)
with tab2:
    st.dataframe(notes.head(10), use_container_width=True)
with tab3:
    st.dataframe(experiments.head(10), use_container_width=True)
with tab4:
    st.dataframe(metrics.head(10), use_container_width=True)
