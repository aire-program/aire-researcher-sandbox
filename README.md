# AIRE Researcher Sandbox
Applied AI Innovation & Research Enablement (AIRE) Program  
Research-Facing Training and Experimentation Environment for AI-Enabled Scholarly Workflows

This repository provides a public, learning-oriented edition of the AIRE Researcher Sandbox originally deployed on internal systems within the College of Social Science at Michigan State University. The internal version is used by research teams, graduate students, and faculty who require a structured, reproducible environment for experimenting with AI-enabled research workflows.

This public edition maintains the internal environment’s instructional structure, research workflows, validation patterns, and governance approach while using small instructional datasets suitable for open distribution. It is provided on GitHub to support transparency, reproducibility, collaboration, and cross-institutional learning.

## Purpose of the Sandbox

The AIRE Researcher Sandbox provides a controlled, notebook-first environment where researchers can:

- explore foundational AI-enabled text and tabular workflows  
- test preprocessing, feature extraction, and vectorization strategies  
- experiment with embeddings and basic semantic search  
- build exploratory prototypes before moving to production or lab-scale systems  
- understand how validation, reproducibility, and governance integrate into research computing  
- practice responsible, well-documented research workflows through guided, hands-on examples  

This environment is one pillar of the AIRE Program and supports research-focused experimentation and methodological learning.

## Who This Sandbox Is For

The Sandbox is designed for:

- research faculty  
- research labs and centers  
- graduate students  
- applied research teams  
- analysts and research software contributors  

It serves researchers who are experienced in their domain but may be new to AI or computational methods. All notebooks follow a clear WHAT / WHY / HOW instructional pattern to support motivated learners.

## What You Can Do in This Environment

### Text Workflows
- Clean, normalize, and prepare text for analysis  
- Extract features using TF-IDF or bag-of-words  
- Experiment with embeddings and document similarity  
- Build simple semantic search prototypes  
- Explore clustering or grouping of documents  
- Validate text preprocessing decisions  

### Tabular Workflows
- Load and inspect example tabular datasets  
- Perform basic feature engineering  
- Train simple baseline classification or regression models  
- Evaluate model behavior using standard metrics  
- Practice reproducible dataset splitting and validation patterns  

### Reproducibility and Governance
- Validate data structures using JSON Schemas  
- Review provenance documentation  
- Apply responsible-use guidelines to early-stage experiments  
- Incorporate governance-aligned templates into research workflows  

All workflows use small instructional datasets appropriate for open distribution.

## Research Modules (Notebooks)

These guided modules introduce core concepts and methods for AI-enabled scholarly workflows. Each module is Colab-friendly and follows a WHAT / WHY / HOW pattern.

### 1. Text Cleaning and Preparation
WHAT: Foundational text preprocessing steps including normalization and tokenization.  
WHY: Clean text is essential for similarity, clustering, and modeling tasks.  
HOW: Apply standard preprocessing, evaluate results, and understand downstream effects.

### 2. Text Feature Extraction (TF-IDF and Vectorization)
WHAT: Converting text documents into numerical feature vectors.  
WHY: Numerical features support similarity comparisons, clustering, and modeling.  
HOW: Generate TF-IDF matrices, inspect sparsity, and evaluate interpretability.

### 3. Embeddings Basics
WHAT: Introduction to dense vector representations of text.  
WHY: Embeddings enable semantic similarity and retrieval workflows.  
HOW: Compute embeddings, explore nearest neighbors, and compare approaches.

### 4. Semantic Search Fundamentals
WHAT: Building a basic semantic search pipeline.  
WHY: Semantic search supports navigation of research corpora.  
HOW: Compute similarity scores, rank documents, and evaluate retrieval results.

### 5. Tabular Data Basics
WHAT: Inspection and exploration of tabular datasets.  
WHY: Foundational exploration supports modeling and inference.  
HOW: Load datasets, explore distributions, validate structure, and assess assumptions.

### 6. Tabular Modeling Foundations
WHAT: Introducing baseline models in scikit-learn.  
WHY: Baseline models clarify how features relate to outcomes.  
HOW: Split datasets, train models, interpret metrics, and evaluate validation patterns.

### 7. Schema Validation and Data Integrity
WHAT: Dataset validation using JSON Schema.  
WHY: Data integrity is essential for stable research pipelines.  
HOW: Load schemas, validate datasets, interpret errors, and integrate checks.

## Launch Modules in Google Colab

Each research module can be opened directly in Google Colab. All notebooks contain a Colab-compatible setup cell.

### Text Workflows

**Text Cleaning and Preparation**  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aire-program/aire-researcher-sandbox/blob/main/notebooks/text_cleaning.ipynb)

**TF-IDF Retrieval Index**  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aire-program/aire-researcher-sandbox/blob/main/notebooks/rag_build_index.ipynb)

**Embeddings Basics**  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aire-program/aire-researcher-sandbox/blob/main/notebooks/embeddings_basics.ipynb)

**Semantic Search Fundamentals**  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aire-program/aire-researcher-sandbox/blob/main/notebooks/semantic_search.ipynb)

### Tabular Workflows

**Tabular Data Basics**  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aire-program/aire-researcher-sandbox/blob/main/notebooks/tabular_basics.ipynb)

**Tabular Modeling Foundations**  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aire-program/aire-researcher-sandbox/blob/main/notebooks/tabular_modeling.ipynb)

### Reproducibility & Governance

**Schema Validation and Data Integrity**  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aire-program/aire-researcher-sandbox/blob/main/notebooks/data_validation.ipynb)

Additional Colab-ready modules are indexed in `docs/colab_index.md` (e.g., `text_classification.ipynb`, `batch_summarization.ipynb`, `rag_query.ipynb`, `rag_evaluation.ipynb`, `minimal_research_assistant.ipynb`, and `rest_api_example.ipynb`).

## Directory Structure

The repository uses the following layout (shown in plain text):

    aire-researcher-sandbox/
        README.md
        requirements.txt
        LICENSE
        notebooks/
        data/
            sample_texts/
            sample_tabular/
            schemas/
        pipelines/
        scripts/
        governance/
        docs/
        tests/
        .github/
            workflows/

## Origin and Public Migration

The AIRE Researcher Sandbox was originally deployed on internal MSU systems as part of the Applied AI Innovation & Research Enablement (AIRE) Program. It served as a controlled environment where research teams could rehearse methods, test workflows, and train new researchers in AI-enabled approaches.

This GitHub edition was created to:

- support transparent sharing of research workflows  
- enable reproducibility and collaborative development  
- offer a publicly accessible learning environment aligned with institutional practices  
- provide a safe training space that mirrors internal expectations without relying on institutional data  

The public version maintains the same workflow philosophy, governance alignment, and instructional structure as the internal system.

## Running the Sandbox

### 1. Install dependencies
    pip install -r requirements.txt

### 2. Optional: run validation scripts
    python scripts/data_loader.py

### 3. Run notebooks locally
    jupyter notebook

### 4. Run in Google Colab
Each notebook includes:
- a Colab-compatible detection cell  
- environment setup instructions  
- links provided in this README and in “docs/colab_index.md”

## Governance and Responsible Use

The Sandbox includes governance materials derived from institutional practices:

- provenance documentation  
- responsible-use guidelines  
- model card templates  
- review and validation checklists  

These materials help researchers integrate responsible AI practices into early-stage experimentation.

## Relationship to Other AIRE Program Components

The AIRE Researcher Sandbox is one part of a multi-pillar institutional initiative:

- The Applied AI Literacy Hub offers institution-wide training and responsible-use foundations.  
- The AIRE Researcher Sandbox supports research-facing experimentation and instruction.  
- The AIRE Impact Dashboard (mirrored in a separate repository) provides analytics and program evaluation.

Each pillar addresses a distinct need while aligning with shared principles of transparency, governance, and reproducibility.

## License

MIT License. See “LICENSE” for details.
