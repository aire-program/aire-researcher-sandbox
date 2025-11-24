# Responsible Use Guidelines

Use these guidelines when working with the AI Researcher Developer Sandbox or adapting workflows to institutional projects.

## Appropriate uses
- Exploratory analysis with synthetic or de-identified data.
- Prototyping retrieval, clustering, or summarization pipelines before applying them to sensitive sources.
- Documenting methods and decisions in the provided governance templates.

## Inappropriate uses
- Uploading personally identifiable or confidential data into unapproved tools or services.
- Presenting synthetic results as if they come from real participants or operational systems.
- Bypassing required reviews (data governance, IRB, or security) for production deployments.

## Sensitive data considerations
- Keep sensitive datasets out of the sandbox; substitute synthetic data whenever possible.
- If working with restricted data elsewhere, mirror only schemas and shapes in this repository.
- Verify that storage locations, access controls, and audit trails meet institutional requirements before handling real data.

## Transparency and documentation
- Disclose when AI tools or synthetic data are used in analyses or publications.
- Maintain versioned records of data generation (seeds, scripts) and model choices.
- Use the provenance, model card, and release checklist templates to capture decisions and known limitations.
