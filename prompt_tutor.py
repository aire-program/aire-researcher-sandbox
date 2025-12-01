import json
from typing import Any, Dict

from aire_llm_client import chat_completion



import os

def _load_system_prompt() -> str:
    """Load the system prompt from the external text file."""
    prompt_path = os.path.join(os.path.dirname(__file__), "prompts", "tutor_system_prompt.txt")
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        # Fallback if file is missing, though this should ideally raise an error
        return "You are a prompt tutor. Respond with JSON scores."

SYSTEM_PROMPT = _load_system_prompt()



def evaluate_prompt(prompt_text: str, learner_role: str) -> Dict[str, Any]:
    """
    Evaluate a prompt against the rubric and return the parsed JSON response.
    """
    user_content = (
        f"Learner role: {learner_role}\n"
        f"Prompt to evaluate:\n{prompt_text}\n"
        "Return only the JSON object."
    )
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_content},
    ]

    raw_response = chat_completion(messages)
    try:
        return json.loads(raw_response)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Failed to parse evaluation JSON") from exc
