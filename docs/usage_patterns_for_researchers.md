# Usage Patterns for Researchers

**What**: Scenario-based starting points that map sandbox resources to common institutional needs.  
**Why**: Clear, role-oriented paths reduce onboarding time and keep analyses consistent with AIRE reporting.  
**How**: Select the role closest to your use case and follow the first-hour path in notebooks or CLI scripts. All flows rely on synthetic data that mirrors the internal AIRE deployment.

## Faculty member reviewing workshop signals
Open `notebooks/text_classification.ipynb` to group synthetic workshop notes and abstracts with TF-IDF + k-means, then review cleaned snippets and cluster labels that inform program design.

**First hour path**
1. Run `scripts/generate_synthetic_data.py`.
2. Open `notebooks/text_cleaning.ipynb` to normalize workshop notes.
3. Run `notebooks/text_classification.ipynb` to surface themes.
4. Browse cleaned narratives and cluster assignments in the notebook outputs.

## Graduate student validating retrieval-assisted usage views
Build a TF-IDF index with `notebooks/rag_build_index.ipynb`, query it in `notebooks/rag_query.ipynb`, and preview ranked content in `notebooks/minimal_research_assistant.ipynb`.

**First hour path**
1. Build the index with `notebooks/rag_build_index.ipynb`.
2. Test questions in `notebooks/rag_query.ipynb`.
3. Preview ranked excerpts in `notebooks/minimal_research_assistant.ipynb`.
4. Review the ranked evidence within the notebook outputs.

## Research staff preparing leadership materials
Browse `notebooks/tabular_basics.ipynb` and `notebooks/tabular_modeling.ipynb` to confirm adoption and confidence aggregates, then adapt the governance templates in **API and Governance Resources** to document provenance and limitations.

**First hour path**
1. Run `notebooks/tabular_basics.ipynb` to validate synthetic adoption signals.
2. Extend indicators in `notebooks/tabular_modeling.ipynb`.
3. Read `governance/responsible_use_guidelines.md` for expected practices.
4. Capture provenance and assumptions with `governance/data_provenance_template.md` and `governance/model_card_template.md`.

## Choose your path (quick matrix)
| Goal | Primary notebook | Governance touchpoint |
| --- | --- | --- |
| Summarize workshop narratives | `notebooks/text_cleaning.ipynb` → `notebooks/text_classification.ipynb` | Start provenance after first run |
| Validate adoption/usage indicators | `notebooks/tabular_basics.ipynb` → `notebooks/tabular_modeling.ipynb` | Capture assumptions for each metric |
| Review retrieval-assisted usage patterns | `notebooks/rag_build_index.ipynb` → `notebooks/rag_query.ipynb` | Note index scope/assumptions in provenance |
| Prototype assistant for ranked evidence | `notebooks/minimal_research_assistant.ipynb` | Complete model card before sharing |
| Confirm API patterns | `notebooks/rest_api_example.ipynb` or `notebooks/embeddings_basics.ipynb` | Reference responsible_use_guidelines.md |
