import pandas as pd
import streamlit as st
from app.config import ARTICLES_PATH, NOTES_PATH, EXPERIMENTS_PATH, METRICS_PATH

@st.cache_data
def load_articles():
    return pd.read_csv(ARTICLES_PATH)

@st.cache_data
def load_notes():
    return pd.read_csv(NOTES_PATH)

@st.cache_data
def load_experiments():
    return pd.read_csv(EXPERIMENTS_PATH)

@st.cache_data
def load_metrics():
    return pd.read_csv(METRICS_PATH)
