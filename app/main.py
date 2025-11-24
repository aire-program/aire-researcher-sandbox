"""Minimal Streamlit workbench entry point."""

from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

# Ensure project root is on path for app imports
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from app.layout import render_header, render_sidebar  # noqa: E402

st.set_page_config(page_title="AIRE Researcher Sandbox", page_icon="🔬", layout="wide")


def main() -> None:
    """Render landing page content."""
    render_sidebar()
    render_header(
        "AI Researcher Developer Sandbox",
        "A minimal research workbench for synthetic, notebook-first workflows.",
    )

    st.markdown(
        """
        This Streamlit app is a thin workbench that mirrors the notebook-first pipelines in this
        repository. It is intentionally minimal: use it to browse synthetic data, try small
        retrieval workflows, and jump into the corresponding notebooks for deeper exploration.

        **Quick links**
        - Generate or refresh data: `python scripts/generate_synthetic_data.py`
        - Run notebooks locally or via the Colab links in `docs/colab_index.md`
        - Explore the navigation tabs above for text, tabular, retrieval, and governance resources
        """
    )


if __name__ == "__main__":
    main()
