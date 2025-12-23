"""OpenAI LLM client wrapper for simplified API interactions."""

from __future__ import annotations

import os
from typing import Any

from openai import OpenAI

_DEFAULT_MODEL = "gpt-4o-mini"


def _get_client() -> OpenAI:
    """Create an OpenAI client using the API key from environment."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY environment variable")
    return OpenAI(api_key=api_key)


def chat_completion(
    messages: list[dict[str, Any]],
    model: str = _DEFAULT_MODEL,
) -> str:
    """Send a chat completion request and return the assistant response."""
    client = _get_client()
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content


def call_llm(prompt_text: str) -> str:
    """Call the LLM with a simple user prompt and default system context."""
    messages = [
        {"role": "system", "content": "You are a concise AI assistant."},
        {"role": "user", "content": prompt_text},
    ]
    return chat_completion(messages)
