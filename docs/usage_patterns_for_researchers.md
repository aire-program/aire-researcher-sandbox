# Usage Patterns for Researchers

**What**: Scenario-based starting points that map Sandbox resources to common research needs.  
**Why**: Quick, concrete paths reduce onboarding time for teams new to applied AI workflows.  
**How**: Select the role closest to your use case, follow the first-hour path, and mirror the same steps in notebooks or the Streamlit workbench. All flows rely on synthetic data that mirrors the internal AIRE deployment.

## Faculty member exploring clustering
A faculty researcher can open `notebooks/text_classification.ipynb` to group synthetic article abstracts with TF-IDF + k-means, then use the Streamlit **Text Workflows** page to spot-check clusters and cleaned snippets.

**First hour path**
1. Run `scripts/generate_synthetic_data.py`.
2. Open `notebooks/text_cleaning.ipynb` to normalize text.
3. Run `notebooks/text_classification.ipynb` to create clusters.
4. Open the Streamlit **Text Workflows** page to browse clusters and cleaned abstracts.

## Graduate student prototyping a retrieval assistant
A graduate student can build a TF-IDF index with `notebooks/rag_build_index.ipynb`, query it in `notebooks/rag_query.ipynb`, and stitch results into templated answers in `notebooks/minimal_research_assistant.ipynb`. The Streamlit **RAG Workbench** mirrors the same retrieval flow for quick iteration.

**First hour path**
1. Build the index with `notebooks/rag_build_index.ipynb`.
2. Experiment with queries in `notebooks/rag_query.ipynb`.
3. Prototype answers in `notebooks/minimal_research_assistant.ipynb`.
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
| Clean and cluster text | `notebooks/text_cleaning.ipynb` → `notebooks/text_classification.ipynb` | **Text Workflows** | Start provenance after first run |
| Clean and feature engineer tabular data | `notebooks/tabular_basics.ipynb` → `notebooks/tabular_modeling.ipynb` | **Tabular Workflows** | Capture provenance for transformations |
| Build/query retrieval | `notebooks/rag_build_index.ipynb` → `notebooks/rag_query.ipynb` | **RAG Workbench** | Note index scope/assumptions in provenance |
| Prototype assistant | `notebooks/minimal_research_assistant.ipynb` | **RAG Workbench** (retrieval view) | Complete model card before sharing |
| API patterns | `notebooks/rest_api_example.ipynb` or `notebooks/embeddings_basics.ipynb` | **API and Governance Resources** | Reference responsible_use_guidelines.md |
