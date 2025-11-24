# Usage Patterns for Researchers

**What**: Scenario-based starting points that map Sandbox resources to common research needs.  
**Why**: Quick, concrete paths reduce onboarding time for teams new to applied AI workflows.  
**How**: Select the role closest to your use case, follow the first-hour path, and mirror the same steps in notebooks or the Streamlit workbench. All flows rely on synthetic data that mirrors the internal AIRE deployment.

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

## Choose your path (quick matrix)
| Goal | Primary notebook | Matching Streamlit page | Governance touchpoint |
| --- | --- | --- | --- |
| Clean and cluster text | `pipelines/text/ingest_and_clean.ipynb` → `pipelines/text/clustering_and_topics.ipynb` | **Text Workflows** | Start provenance after first run |
| Clean and feature engineer tabular data | `pipelines/tabular/tabular_cleaning.ipynb` → `pipelines/tabular/feature_engineering.ipynb` | **Tabular Workflows** | Capture provenance for transformations |
| Build/query retrieval | `pipelines/rag/build_index.ipynb` → `pipelines/rag/rag_query.ipynb` | **RAG Workbench** | Note index scope/assumptions in provenance |
| Prototype assistant | `pipelines/prototypes/minimal_research_assistant.ipynb` | **RAG Workbench** (retrieval view) | Complete model card before sharing |
| API patterns | `api/notebooks/rest_api_example.ipynb` or `api/notebooks/embeddings_api_example.ipynb` | **API and Governance Resources** | Reference responsible_use_guidelines.md |
