"""Links to API examples and governance templates."""

from __future__ import annotations

from pathlib import Path

import streamlit as st

from app import config
from app.layout import render_header


GOVERNANCE_FILES = [
    "responsible_use_guidelines.md",
    "data_provenance_template.md",
    "model_card_template.md",
    "review_before_release_checklist.md",
]


def _read_markdown(path: Path) -> str:
    if not path.exists():
        return "File not found."
    return path.read_text(encoding="utf-8")


def main() -> None:
    render_header("API and Governance Resources", "Jump into notebooks and review templates.")
    st.markdown(
        "This page gathers links to API demonstrations and the governance templates you can adapt. "
        "It matters because technical experiments should travel with clear documentation and safe practices. "
        "Open a notebook to explore client patterns, then view the templates to record provenance and intended use."
    )

    st.markdown("### API example notebooks")
    st.markdown(
        "- [REST API example](https://colab.research.google.com/github/aire-program/aire-researcher-sandbox/blob/main/api/notebooks/rest_api_example.ipynb)"
    )
    st.markdown(
        "- [Embeddings API example](https://colab.research.google.com/github/aire-program/aire-researcher-sandbox/blob/main/api/notebooks/embeddings_api_example.ipynb)"
    )
    st.markdown(
        "- All notebooks are runnable locally and include a Colab setup cell for quick starts."
    )

    st.markdown("### Governance templates")
    selected_doc = st.selectbox("View a governance resource", GOVERNANCE_FILES)
    content = _read_markdown(config.GOVERNANCE_DIR / selected_doc)
    st.markdown(content)

    st.info(
        "Governance assets are provided as templates. Adapt them to your own research context to "
        "document provenance, intended use, and responsible release checks."
    )
    st.caption(
        "Next steps: explore api/notebooks/rest_api_example.ipynb and api/notebooks/embeddings_api_example.ipynb via Colab, "
        "then tailor governance templates before sharing prototypes."
    )


if __name__ == "__main__":
    main()
