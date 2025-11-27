import os
from typing import List, Tuple

import nbformat

SKIP_DIRS = {".git", "venv", ".venv"}


def discover_notebooks(root: str) -> List[str]:
    notebooks = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for filename in filenames:
            if filename.endswith(".ipynb"):
                notebooks.append(os.path.join(dirpath, filename))
    return notebooks


def has_micro_tutor(nb) -> bool:
    markers = (
        "AIRE Micro Tutor",
        "prompt_tutor",
        "aire_telemetry",
        "resources_map",
    )
    for cell in nb.cells:
        source = cell.get("source", "")
        if any(marker in source for marker in markers):
            return True
    return False


def identity_cell(file_path: str):
    resource_id = f"notebook:{os.path.splitext(os.path.basename(file_path))[0]}"
    source = "\n".join(
        [
            "# AIRE Micro Tutor Identity Cell",
            "import datetime as dt",
            "learner_id = input('Enter your learner ID (email or handle): ').strip()",
            "learner_role = input('Enter your learner role (e.g., researcher, educator): ').strip()",
            f"resource_id = '{resource_id}'",
            "session_id = f\"{learner_id}-{dt.datetime.utcnow().isoformat()}\"",
        ]
    )
    return nbformat.v4.new_code_cell(source=source)


def imports_cell():
    source = "\n".join(
        [
            "# AIRE Micro Tutor Imports",
            "from prompt_tutor import evaluate_prompt",
            "from aire_telemetry import log_event",
            "from resources_map import RESOURCE_MAP",
        ]
    )
    return nbformat.v4.new_code_cell(source=source)


def micro_tutor_cell():
    source = "\n".join(
        [
            "# AIRE Micro Tutor Prompt + Feedback Cell",
            "from aire_llm_client import chat_completion",
            "",
            "def call_llm(prompt_text: str) -> str:",
            "    messages = [",
            "        {'role': 'system', 'content': 'You are an AI helper responding concisely.'},",
            "        {'role': 'user', 'content': prompt_text},",
            "    ]",
            "    return chat_completion(messages)",
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
        ]
    )
    return nbformat.v4.new_code_cell(source=source)


def upgrade_notebook(path: str) -> Tuple[bool, str]:
    nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)
    if has_micro_tutor(nb):
        return False, "skipped (micro tutor already present)"

    nb.cells.insert(0, imports_cell())
    nb.cells.insert(0, identity_cell(path))
    nb.cells.append(micro_tutor_cell())

    nbformat.write(nb, path)
    return True, "upgraded"


def main():
    root = os.getcwd()
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
