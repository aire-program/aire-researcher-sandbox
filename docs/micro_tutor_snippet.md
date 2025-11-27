# Micro Tutor Snippet

The Micro Tutor snippet is a minimal, copy-paste set of cells that lets you evaluate and refine prompts inside a notebook while capturing lightweight telemetry. It shows how to keep identity info, imports, and the evaluation workflow together without extra scaffolding.

## Identity cell
- Purpose: declare who you are and how the tutor should interpret your role (e.g., researcher, educator). Keep it short but descriptive so downstream evaluations have context.
- Typical contents: `learner_role` string plus any identifiers needed for telemetry (email, initials, or an anonymous session ID).

## Imports cell
- Purpose: load the minimal dependencies required to run the tutor workflow without pulling in unnecessary packages.
- Typical contents: `dotenv` to load secrets, the `evaluate_prompt` helper, and any local utilities. Keep it focused to speed up notebook startup.

## Prompt + Tutor + Telemetry cell
- Purpose: hold the actual prompt text, run it through the tutor, and optionally send telemetry about the evaluation.
- Typical contents: the prompt string, a call to `evaluate_prompt(prompt_text, learner_role)`, and a `log_event` call that records the attempt. Keep the cell simple and linear so users can edit the prompt and rerun quickly.
