"""Overview page with dataset counts and navigation tips."""

from __future__ import annotations

import streamlit as st

from app.layout import render_header
from app import utils


def main() -> None:
    render_header("Sandbox Overview", "Synthetic, research-ready datasets at a glance.")

    articles = utils.load_articles()
    notes = utils.load_notes()
    experiments = utils.load_experiments()
    metrics = utils.load_metrics()

    st.markdown("### Dataset quick counts")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Articles", len(articles))
    col2.metric("Notes", len(notes))
    col3.metric("Experiments", len(experiments))
    col4.metric("Metrics", len(metrics))

    st.markdown(
        """
        Use this workbench to preview the synthetic data and jump into the notebook-first workflows.
        Each page mirrors a notebook in the `pipelines/` directory so that experiments remain
        reproducible and well-documented.
        """
    )

    st.markdown("### Where to go next")
    st.markdown("- Text workflows: cleaning and clustering demonstrations")
    st.markdown("- Tabular workflows: sanity checks and feature engineering")
    st.markdown("- RAG workbench: build and query a TF-IDF index")
    st.markdown("- API and governance resources: notebook links and templates")

    st.info(
        "Prefer notebooks? Start with pipelines/text/ingest_and_clean.ipynb or pipelines/tabular/tabular_cleaning.ipynb "
        "for hands-on steps, or use the Colab badges in docs/colab_index.md."
    )


if __name__ == "__main__":
    main()
