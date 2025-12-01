# AIRE Researcher Sandbox  

The AIRE Researcher Sandbox is one component of the Applied AI Innovation and Research Enablement (AIRE) Program. It provides a structured, reproducible environment where researchers, graduate students, and research teams can explore AI-enabled methods through guided, hands-on workflows. The Sandbox was originally deployed on internal MSU systems and later mirrored to GitHub to support transparency, reproducibility, and cross-institutional collaboration. All datasets in the public version are synthetic and suitable for open distribution.

This environment is designed for researchers who are experienced in their discipline but new to AI or computational methods. Each workflow emphasizes clarity, responsible use, and well-documented methodological decisions so that researchers can integrate AI into their work in a thoughtful and well-supported way.

## Role in the AIRE Ecosystem

The AIRE Program includes four coordinated components:

- AIRE Literacy Hub  
- AIRE Researcher Sandbox  
- AIRE Impact Dashboard  
- AIRE Personalization Layer (Micro Tutor and Learner Scorecard)

Within this structure, the AIRE Researcher Sandbox serves as the program’s research-facing experimentation environment. It allows researchers to:

- test AI-enabled workflows in a controlled setting  
- learn and apply responsible research practices  
- rehearse methods before moving to production or lab-scale environments  
- evaluate techniques with small, reproducible datasets  
- understand governance implications of AI-enabled work  
- use the Micro Tutor for prompt-level guidance and iterative refinement  

The Sandbox brings together learning design, experimentation, and responsible research practice in one environment that models clear, transparent methods.

## What You Can Do in This Environment

### Text Workflows
- Clean and prepare raw text  
- Extract features using TF-IDF and vectorization  
- Explore embeddings and semantic similarity  
- Build simple retrieval and ranking pipelines  
- Experiment with clustering and grouping  
- Evaluate preprocessing and representation choices  

### Tabular Workflows
- Load and explore tabular datasets  
- Perform basic feature engineering  
- Train and evaluate baseline models  
- Interpret common metrics  
- Practice reproducible validation strategies  

### Reproducibility and Governance
- Validate data structures with JSON Schema  
- Apply provenance and documentation practices  
- Review responsible-use principles  
- Use governance-aligned templates from the internal program  
- Understand how institutional expectations apply to early-stage AI research  

All workflows use instructional datasets that illustrate method, not scale.

## Micro Tutor Integration

This repository includes the public version of the AIRE Micro Tutor, a lightweight feedback tool embedded directly into Sandbox notebooks. The Micro Tutor provides rubric-based guidance on prompt design using four evaluation categories:

- clarity  
- context  
- constraints  
- evaluation instructions  

Its purpose is to support iterative refinement during experimentation. Each use of the Micro Tutor generates synthetic telemetry (in the public version) that reflects how learners or researchers adjust their prompting practice over time. This telemetry model aligns with the structure used by the AIRE Learner Scorecard and Impact Dashboard.

To enable the Micro Tutor locally, users must create a `.env` file using `.env.example` as a template and supply their own API key. No credentials, internal keys, or MSU-controlled services are included in this public repository.

## Research Modules (Notebooks)

These guided modules introduce core concepts for AI-enabled scholarly work. Each notebook follows a clear instructional pattern and includes Colab-ready setup cells.

### Text Workflows
1. Text Cleaning and Preparation  
2. Text Feature Extraction (TF-IDF and Vectorization)  
3. Embeddings Basics  
4. Semantic Search Fundamentals  

### Tabular Workflows
5. Tabular Data Basics  
6. Tabular Modeling Foundations  

### Reproducibility and Governance
7. Schema Validation and Data Integrity  

Additional modules such as text classification, summarization, evaluation workflows, retrieval experiments, and API-based examples are included in the `notebooks/` directory and indexed in `docs/colab_index.md`.

## Launching Modules in Google Colab

Each notebook contains a Colab-compatible setup cell and can be launched directly from the links provided in this README and in the `docs/colab_index.md` index. These notebooks support workflows for learners who prefer running experiments in a hosted environment without local installation.

## Directory Structure

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

This structure mirrors the internal MSU deployment while using synthetic datasets and simplified pipelines for public distribution.

## Running the Sandbox Locally

1. Install dependencies  
       pip install -r requirements.txt

2. (Optional) Run validation scripts  
       python scripts/data_loader.py

3. Start Jupyter Notebook  
       jupyter notebook

4. Alternatively, open any module directly in Google Colab using the links included in this repository.

## Responsible Use and Governance Alignment

The AIRE Program emphasizes responsible AI practice. This repository includes governance resources that reflect internal MSU expectations for early-stage research experimentation, including:

- provenance documentation  
- model card templates  
- review and validation checklists  
- responsible-use considerations for AI workflows  

These materials help research teams integrate responsible and well-governed methods into exploratory work.

## Relationship to Other AIRE Components

The AIRE Researcher Sandbox is connected to the other pillars of the program:

- The AIRE Literacy Hub provides foundational tutorials and learning materials.  
- The Sandbox builds on those foundations to support methodological exploration.  
- The AIRE Impact Dashboard (mirrored separately) models institutional analytics derived from program participation.  
- The AIRE Personalization Layer links prompt-level feedback (Micro Tutor) with learner-facing analytics (Learner Scorecard).  

Together, these components form a comprehensive support structure for responsible AI adoption across the college.

## License

MIT License. See the included LICENSE file for details.
