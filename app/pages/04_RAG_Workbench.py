"""Simple retrieval workbench using TF-IDF."""

from __future__ import annotations

from typing import Any, List, Tuple

import pandas as pd
import streamlit as st

from app import utils
from app.layout import render_header


@st.cache_resource
def _build_index(df: pd.DataFrame) -> Tuple[Any, Any]:
    """Build and cache a TF-IDF index."""
    return utils.build_tfidf_index(df["abstract"].fillna(""))


def _format_excerpt(text: str, length: int = 220) -> str:
    snippet = text[:length].rsplit(" ", 1)[0]
    return snippet + "..." if snippet else text


def main() -> None:
    render_header("RAG Workbench", "Lightweight retrieval over synthetic abstracts.")

    articles = utils.load_articles()
    vectorizer, matrix = _build_index(articles)

    query = st.text_input("Enter a research question", value="What methods support reproducible AI?")
    if query:
        scores = utils.query_index(query, vectorizer, matrix)
        articles = articles.assign(score=scores)
        top_hits = articles.sort_values("score", ascending=False).head(5)

        st.markdown("### Top matches")
        for _, row in top_hits.iterrows():
            st.markdown(f"**{row['title']}** (score: {row['score']:.3f})")
            st.caption(_format_excerpt(row["abstract"]))
            st.markdown("---")

    st.info(
        "This page mirrors the retrieval workflows in `pipelines/rag`. Use the notebooks to extend the "
        "indexing strategy, add evaluation cells, or swap in alternative vectorizers."
    )
    st.caption(
        "Next steps: pipelines/rag/build_index.ipynb to create the index, pipelines/rag/rag_query.ipynb to test queries, "
        "and pipelines/rag/rag_evaluation.ipynb for quick relevance comparisons."
    )


if __name__ == "__main__":
    main()
