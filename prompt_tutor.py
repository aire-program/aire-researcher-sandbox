"""Prompt evaluation utilities using LLM-based rubric scoring."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from aire_llm_client import chat_completion

_PROMPTS_DIR = Path(__file__).parent / "prompts"


def _load_system_prompt() -> str:
    """Load the tutor system prompt from the external text file."""
    prompt_path = _PROMPTS_DIR / "tutor_system_prompt.txt"
    if not prompt_path.exists():
        raise FileNotFoundError(f"System prompt not found: {prompt_path}")
    return prompt_path.read_text(encoding="utf-8").strip()


SYSTEM_PROMPT = _load_system_prompt()


def evaluate_prompt(prompt_text: str, learner_role: str) -> dict[str, Any]:
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
