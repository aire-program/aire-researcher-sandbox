"""Text workflow exploration page."""

from __future__ import annotations

from typing import Tuple

import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

from app import utils
from app.layout import render_header


@st.cache_resource
def _cluster_articles(df: pd.DataFrame, n_clusters: int = 4) -> Tuple[pd.Series, TfidfVectorizer]:
    """Cluster articles using TF-IDF + k-means."""
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(df["abstract"].fillna(""))
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = model.fit_predict(matrix)
    return pd.Series(labels, index=df.index), vectorizer


def main() -> None:
    render_header("Text Workflows", "Quick exploration of the synthetic article corpus.")

    articles = utils.load_articles()
    notes = utils.load_notes()

    view_choice = st.radio("Select dataset", ("Articles", "Notes"), horizontal=True)

    if view_choice == "Articles":
        labels, _ = _cluster_articles(articles)
        articles = articles.assign(cluster=labels)
        st.markdown("Choose a sample article to view a cleaned snippet and its cluster assignment.")
        selection = st.selectbox("Article", articles["title"].tolist())
        selected_row = articles[articles["title"] == selection].iloc[0]

        cleaned = utils.clean_text(selected_row["abstract"])
        st.write("**Cluster**", int(selected_row["cluster"]))
        st.write("**Original abstract**")
        st.write(selected_row["abstract"])
        st.write("**Cleaned abstract**")
        st.write(cleaned)
    else:
        st.markdown("Choose a research note to preview quick cleaning.")
        selection = st.selectbox("Note", notes["note_id"].tolist())
        selected_row = notes[notes["note_id"] == selection].iloc[0]
        cleaned = utils.clean_text(selected_row["note_text"])
        st.write("**Original note**")
        st.write(selected_row["note_text"])
        st.write("**Cleaned note**")
        st.write(cleaned)

    st.info(
        "These operations mirror the notebook workflows in `pipelines/text`, where you can run full "
        "cleaning, clustering, and summarization steps with the same synthetic data."
    )


if __name__ == "__main__":
    main()
