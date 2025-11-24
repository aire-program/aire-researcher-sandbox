# Review Before Release Checklist

**Mandatory Review**: This checklist must be completed prior to the distribution of any notebooks, models, or research findings derived from this sandbox.

## Objective
To ensure that all released artifacts meet institutional standards for data privacy, documentation, and ethical compliance. Releases must pair results with adequate context to prevent misinterpretation.

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
