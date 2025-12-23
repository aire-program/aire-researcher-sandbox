"""Upgrade Jupyter notebooks with AIRE Micro Tutor cells."""

from __future__ import annotations

from pathlib import Path

import nbformat

_SKIP_DIRS = frozenset({".git", "venv", ".venv", "__pycache__", "node_modules"})

_TUTOR_MARKERS = (
    "AIRE Micro Tutor",
    "prompt_tutor",
    "aire_telemetry",
    "resources_map",
)


def discover_notebooks(root: Path) -> list[Path]:
    """Find all Jupyter notebooks in the directory tree."""
    notebooks = []
    for path in root.rglob("*.ipynb"):
        if not any(skip in path.parts for skip in _SKIP_DIRS):
            notebooks.append(path)
    return notebooks


def _has_micro_tutor(nb: nbformat.NotebookNode) -> bool:
    """Check if notebook already contains micro tutor cells."""
    for cell in nb.cells:
        source = cell.get("source", "")
        if any(marker in source for marker in _TUTOR_MARKERS):
            return True
    return False


def _identity_cell(file_path: Path) -> nbformat.NotebookNode:
    """Create the learner identity input cell."""
    resource_id = f"notebook:{file_path.stem}"
    source = "\n".join([
        "# AIRE Micro Tutor Identity Cell",
        "import datetime as dt",
        "learner_id = input('Enter your learner ID (email or handle): ').strip()",
        "learner_role = input('Enter your learner role (e.g., researcher, educator): ').strip()",
        f"resource_id = '{resource_id}'",
        'session_id = f"{learner_id}-{dt.datetime.utcnow().isoformat()}"',
    ])
    return nbformat.v4.new_code_cell(source=source)


def _imports_cell() -> nbformat.NotebookNode:
    """Create the imports cell."""
    source = "\n".join([
        "# AIRE Micro Tutor Imports",
        "from prompt_tutor import evaluate_prompt",
        "from aire_telemetry import log_event",
        "from resources_map import RESOURCE_MAP",
    ])
    return nbformat.v4.new_code_cell(source=source)


def _micro_tutor_cell() -> nbformat.NotebookNode:
    """Create the prompt evaluation and feedback cell."""
    source = "\n".join([
        "# AIRE Micro Tutor Prompt + Feedback Cell",
        "from aire_llm_client import call_llm",
        "",
        "prompt_text = input('Enter the prompt you want to test: ').strip()",
        "ai_response = call_llm(prompt_text)",
        "evaluation = evaluate_prompt(prompt_text, learner_role)",
        "",
        "clarity = evaluation.get('clarity_score')",
        "context = evaluation.get('context_score')",
        "constraints = evaluation.get('constraints_score')",
        "evaluation_score = evaluation.get('evaluation_score')",
        "primary_weakness = evaluation.get('primary_weakness', '')",
        "recommended_resource_id = RESOURCE_MAP.get(primary_weakness) or RESOURCE_MAP.get('evaluation')",
        "",
        "log_event(",
        "    event_name='micro_tutor_evaluation',",
        "    user_id=learner_id or session_id,",
        "    metadata={",
        "        'resource_id': resource_id,",
        "        'learner_role': learner_role,",
        "        'clarity': clarity,",
        "        'context': context,",
        "        'constraints': constraints,",
        "        'evaluation_score': evaluation_score,",
        "        'primary_weakness': primary_weakness,",
        "    },",
        ")",
        "",
        "print('\\n--- AI Response ---')",
        "print(ai_response)",
        "print('\\n--- Feedback ---')",
        "print(evaluation.get('summary', 'No summary provided.'))",
        "print('Primary weakness:', primary_weakness or 'n/a')",
        "print('Strengths:', ', '.join(evaluation.get('strengths', [])) or 'n/a')",
        "print('Suggestions:', ', '.join(evaluation.get('suggestions', [])) or 'n/a')",
        "print('\\nRecommended resource:', recommended_resource_id or 'n/a')",
    ])
    return nbformat.v4.new_code_cell(source=source)


def upgrade_notebook(path: Path) -> tuple[bool, str]:
    """Add micro tutor cells to a notebook if not already present."""
    nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)
    if _has_micro_tutor(nb):
        return False, "skipped (already present)"

    nb.cells.insert(0, _imports_cell())
    nb.cells.insert(0, _identity_cell(path))
    nb.cells.append(_micro_tutor_cell())

    nbformat.write(nb, path)
    return True, "upgraded"


def main() -> None:
    """Upgrade all notebooks in the current directory."""
    root = Path.cwd()
    notebooks = discover_notebooks(root)
    upgraded = 0
    skipped = 0

    for nb_path in notebooks:
        changed, message = upgrade_notebook(nb_path)
        if changed:
            upgraded += 1
        else:
            skipped += 1
        print(f"{nb_path}: {message}")

    print(f"\nSummary: upgraded {upgraded}, skipped {skipped}, total {len(notebooks)}")


if __name__ == "__main__":
    main()
