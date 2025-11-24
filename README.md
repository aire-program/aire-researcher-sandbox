AI Researcher Developer Sandbox  
AIRE Program – Applied AI Innovation & Research Enablement, College of Social Science, Michigan State University  

The AI Researcher Developer Sandbox is part of the Applied AI Innovation & Research Enablement (AIRE) Program, an institutional initiative in the College of Social Science at Michigan State University. The program was created to support responsible, evidence-based AI adoption across teaching, learning, and research.

Originally developed and deployed on Michigan State University’s internal GitLab environment, this repository provides a public, synthetic-data mirror of the Sandbox to support collaboration, transparency, and alignment with community standards for responsible AI integration.

Executive Summary  
The AI Researcher Developer Sandbox was designed to meet a growing institutional need: researchers required a safe, reproducible, and well-governed environment for experimenting with AI-enabled research workflows.

While the Applied AI Literacy Hub focuses on responsible use and pedagogical integration, the Sandbox provides a technical space where researchers can:

- prototype AI-assisted research tools  
- explore data processing and retrieval workflows  
- test responsible retrieval-augmented generation patterns  
- build computational pipelines without risking sensitive data  
- evaluate governance, provenance, and documentation practices  

The Sandbox serves as the research-facing counterpart to the AIRE Program, providing a reproducible technical foundation that supports faculty, graduate researchers, and research centers as they adapt AI into scholarly workflows.

Goals and Institutional Rationale  
1. A reproducible environment for AI-enabled scholarship  
2. A policy-aligned space for experimentation  
3. Infrastructure that lowers technical barriers  
4. Support for cross-department collaboration  

Core Components  
1. Reproducible Jupyter Pipelines  
2. Research-Ready API Examples  
3. Safe Retrieval and Indexing Environment  
4. Minimal Streamlit Research Workbench  
5. Governance, Provenance, and Documentation Toolkit  

Synthetic Data and Safety  
All data included in this public release is entirely synthetic and generated programmatically via scripts/generate_synthetic_data.py. The structure of the data mirrors patterns commonly encountered in research environments but contains no real records. This makes the Sandbox safe to explore on local machines and in cloud notebook environments such as Google Colab.

Running the Sandbox Locally  
Clone the repository, create a virtual environment, install requirements, generate synthetic data, and run:

- python scripts/generate_synthetic_data.py  
- streamlit run app/main.py  

You may also open the notebooks in pipelines/ directly in Jupyter to explore individual workflows against the synthetic data.

Optional: Running Selected Notebooks in Google Colab  
Selected pipelines can be launched directly in Google Colab using “Open in Colab” badges listed in docs/colab_index.md. These notebooks are configured with optional setup cells that install required dependencies when executed in Colab. All data used in this repository is synthetic and contains no sensitive or identifiable information.

Relationship to the Applied AI Literacy Hub  
The AI Researcher Developer Sandbox complements the Applied AI Literacy Hub (hosted under the applied-ai-literacy GitHub organization), which provides microcourses and teaching resources for AI literacy. Together with the Applied AI Literacy – Program Impact Dashboard, these projects form a cohesive portfolio that spans pedagogy, research enablement, and institutional analytics.

Testing and CI  
The project includes a pytest suite validating data schemas, API client behavior, and vector index consistency. GitHub Actions workflows run CI and smoke tests on every commit to ensure that dependencies install successfully, tests pass, and core application components can be imported.

Repository Overview  
app/ — Minimal Streamlit research workbench  
pipelines/ — Jupyter AI workflows  
api/ — API clients and demonstration notebooks  
data/ — Synthetic data and schemas  
governance/ — Research governance templates  
scripts/ — Data generation and environment tools  
tests/ — Pytest suite  
docs/ — Extended documentation and Colab index  
.github/workflows — CI pipelines  

License and Openness  
This open GitHub version reflects a broader commitment to reproducible research, transparent workflows, and inter-institutional collaboration around responsible AI integration. The repository is released under the MIT License. See LICENSE for details.
