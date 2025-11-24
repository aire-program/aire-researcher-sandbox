# Usage Patterns for Researchers

## Faculty member exploring clustering
A faculty researcher can open `pipelines/text/clustering_and_topics.ipynb` to group synthetic article abstracts with TF-IDF + k-means, then use the Streamlit **Text Workflows** page to spot-check clusters and cleaned snippets.

## Graduate student prototyping a retrieval assistant
A graduate student can build a TF-IDF index with `pipelines/rag/build_index.ipynb`, query it in `pipelines/rag/rag_query.ipynb`, and stitch results into templated answers in `pipelines/prototypes/minimal_research_assistant.ipynb`. The Streamlit **RAG Workbench** mirrors the same retrieval flow for quick iteration.

## Research staff reviewing governance templates
Research staff can browse `governance/` for provenance, model card, and release checklist templates, or view them inside the **API and Governance Resources** page. These templates can be copied into internal reviews to document data handling and responsible use expectations.
