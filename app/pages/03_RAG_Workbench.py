import streamlit as st
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from app.layout import render_header, render_sidebar
from app.utils import load_articles

st.set_page_config(page_title="RAG Workbench | AIRE Sandbox", page_icon="🔍", layout="wide")

render_sidebar()
render_header()

st.title("RAG Workbench")
st.markdown("Test simple retrieval-augmented generation patterns using TF-IDF on the synthetic articles.")

articles = load_articles()

if not articles.empty:
    # Build Index
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(articles['abstract'].fillna(''))
    
    query = st.text_input("Enter a search query:", "neural networks and social dynamics")
    
    if query:
        query_vec = vectorizer.transform([query])
        cosine_sim = cosine_similarity(query_vec, tfidf_matrix).flatten()
        
        # Get top 5
        top_indices = cosine_sim.argsort()[-5:][::-1]
        
        st.subheader("Top Retrieval Results")
        for idx in top_indices:
            score = cosine_sim[idx]
            if score > 0:
                article = articles.iloc[idx]
                with st.expander(f"{article['title']} (Score: {score:.4f})"):
                    st.markdown(f"**ID:** {article['article_id']}")
                    st.markdown(f"**Abstract:** {article['abstract']}")
            else:
                st.write("No relevant matches found.")
                break
else:
    st.error("No articles data found.")
