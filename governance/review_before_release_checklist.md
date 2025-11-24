# Review Before Release Checklist

**Mandatory Review**: Complete this checklist before distributing any notebooks, models, or research findings derived from the AIRE Researcher Sandbox synthetic mirror.

**What**: A pre-release gate for synthetic-mirror outputs.  
**Why**: Ensures artifacts meet institutional standards for privacy, documentation, and ethical compliance across internal and mirrored environments.  
**How**: Walk through each section, mark completion, and store the checklist with the release package.

## Data Safety
- [ ] Data anonymization or synthesis has been verified; no PII remains.
- [ ] Data provenance is documented using `governance/data_provenance_template.md`.
- [ ] Data license supports the intended distribution and use.

## Model and Workflow Safety
- [ ] Model card is complete and current.
- [ ] Evaluation metrics are documented and reproducible.
- [ ] Bias and fairness checks have been reviewed.

## Documentation
- [ ] README and usage docs are updated for this release.
- [ ] Installation and setup instructions are validated end-to-end.
- [ ] Example notebooks and scripts run from a clean environment.

## Ethical and Compliance Review
- [ ] Ethical/IRB considerations have been addressed where applicable.
- [ ] Security and access controls align with institutional policy.
- [ ] Stakeholders have reviewed risks and limitations.
