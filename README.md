# AIRE Researcher Sandbox
Synthetic-Data Research Environment for AI-Enabled Scholarly Workflows

This repository provides a publicly accessible synthetic-data mirror of the internal AIRE Researcher Sandbox used within the College of Social Science at Michigan State University. The internal system supports research teams, graduate students, and faculty experimenting with AI-enabled research workflows in a safe, reproducible environment. This public mirror maintains the structure, workflows, schemas, and governance patterns of the internal system but uses fully synthetic data to ensure privacy, safety, and unrestricted sharing. Its purpose is to support transparency, reproducibility, collaborative development, and cross-institutional learning.

## Purpose of the Sandbox

The AIRE Researcher Sandbox provides a controlled, notebook-first environment where researchers can:

- explore AI-enabled text and tabular workflows  
- test preprocessing strategies  
- experiment with embeddings and semantic search  
- practice basic modeling and vectorization  
- understand how validation, reproducibility, and governance integrate into research computing  
- develop prototype workflows before scaling them to production systems or research labs  

This environment complements other components of the AIRE Program ecosystem by supporting research-focused experimentation and methodological learning.

## Who This Sandbox Is For

The Sandbox supports researchers who are:

- experienced in their domain but new to AI methods  
- exploring text or tabular analysis workflows  
- evaluating preprocessing or representation strategies  
- developing early prototypes before committing to full pipelines  
- learning how reproducible research practices integrate with AI workflows  

No prior machine learning experience is required. All notebooks follow a “WHAT / WHY / HOW” instructional pattern designed for smart, motivated, but inexperienced researchers.

## What You Can Do in This Environment

### Text Workflows
- Clean and prepare text for analysis  
- Extract features using TF-IDF or bag-of-words methods  
- Explore embeddings and document similarity  
- Build simple semantic search prototypes  
- Run clustering or grouping analyses  
- Validate preprocessing pipelines  

### Tabular Workflows
- Load and inspect experimental or observational datasets  
- Perform basic feature engineering  
- Train simple baseline models  
- Evaluate model behavior using standard metrics  
- Practice dataset splitting and reproducibility patterns  

### Reproducibility and Governance
- Apply schema validation using JSON Schema  
- Review provenance and lifecycle metadata  
- Generate synthetic data using fixed seeds  
- Explore responsible-use documentation patterns  

All workflows use synthetic data structured to mirror the internal AIRE environment.

## Directory Structure

The repository uses the following layout (shown as plain text to preserve copyability):

    aire-researcher-sandbox/
        README.md
        requirements.txt
        LICENSE
        notebooks/               (Colab-friendly research workflows)
        data/
            sample_texts/        (Synthetic text datasets)
            sample_tabular/      (Synthetic tabular datasets)
            schemas/             (JSON Schemas for validation)
        pipelines/               (Modular Python pipeline components)
        scripts/                 (Utility scripts for data loading and validation)
        governance/              (Provenance templates and responsible-use guidelines)
        docs/                    (Additional documentation and walkthroughs)
        tests/                   (Schema, pipeline, and notebook validation tests)
        .github/
            workflows/           (CI: linting, schema checks, notebook execution, tests)

## Synthetic Data Philosophy

The Sandbox uses synthetic datasets that:

- follow the same schema as internal datasets  
- contain no private, sensitive, or institutional data  
- allow unrestricted sharing, experimentation, and redistribution  
- support reproducible instruction and workflow testing  

The synthetic data generator script (“scripts/generate_synthetic_data.py”) uses fixed random seeds and governance-aligned metadata patterns to maintain consistency.

## Running the Sandbox

### 1. Install dependencies

    pip install -r requirements.txt

### 2. Generate synthetic data (optional)

    python scripts/generate_synthetic_data.py

### 3. Run notebooks locally

    jupyter notebook

### 4. Run in Google Colab

Each notebook includes:
- a Colab-compatible first cell
- environment setup instructions  
- links for launching in Colab (see “docs/colab_index.md”)

## Governance and Responsible Use

The Sandbox includes governance templates used in institutional AI workflows:

- provenance documentation  
- model card templates  
- responsible-use guidelines  
- review checklists  

These materials support safe experimentation and help researchers integrate responsible AI practices into their work.

## Complementarity Within the AIRE Program

The AIRE Researcher Sandbox is one part of a multi-pillar program:

- The Applied AI Literacy Hub supports institution-wide training and responsible-use guidance.  
- The AIRE Researcher Sandbox supports research-focused experimentation with synthetic data.  
- The AIRE Impact Dashboard (mirrored separately) supports program-level evaluation and analytics.  

Each component serves a distinct purpose while maintaining a consistent governance and reproducibility philosophy.

## License

MIT License. See “LICENSE” for details.
