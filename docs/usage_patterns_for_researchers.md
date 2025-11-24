# Usage Patterns for Researchers

## Faculty member exploring clustering
A faculty researcher can open `pipelines/text/clustering_and_topics.ipynb` to group synthetic article abstracts with TF-IDF + k-means, then use the Streamlit **Text Workflows** page to spot-check clusters and cleaned snippets.

**First hour path**
1. Run `scripts/generate_synthetic_data.py`.
2. Open `pipelines/text/ingest_and_clean.ipynb` to normalize text.
3. Run `pipelines/text/clustering_and_topics.ipynb` to create clusters.
4. Open the Streamlit **Text Workflows** page to browse clusters and cleaned abstracts.

## Graduate student prototyping a retrieval assistant
A graduate student can build a TF-IDF index with `pipelines/rag/build_index.ipynb`, query it in `pipelines/rag/rag_query.ipynb`, and stitch results into templated answers in `pipelines/prototypes/minimal_research_assistant.ipynb`. The Streamlit **RAG Workbench** mirrors the same retrieval flow for quick iteration.

**First hour path**
1. Build the index with `pipelines/rag/build_index.ipynb`.
2. Experiment with queries in `pipelines/rag/rag_query.ipynb`.
3. Prototype answers in `pipelines/prototypes/minimal_research_assistant.ipynb`.
4. Use the Streamlit **RAG Workbench** to interactively test questions with the same index.

## Research staff reviewing governance templates
Research staff can browse `governance/` for provenance, model card, and release checklist templates, or view them inside the **API and Governance Resources** page. These templates can be copied into internal reviews to document data handling and responsible use expectations.

**First hour path**
1. Read `governance/responsible_use_guidelines.md` for expected practices.
2. Draft data provenance using `governance/data_provenance_template.md` after running a notebook.
3. Fill out `governance/model_card_template.md` before sharing prototype outputs.
4. Run through `governance/review_before_release_checklist.md` to ensure documentation is complete.
