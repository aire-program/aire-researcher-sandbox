import os
from typing import List, Dict, Any

from openai import OpenAI


def _get_client() -> OpenAI:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY environment variable")
    return OpenAI(api_key=api_key)


def chat_completion(messages: List[Dict[str, Any]], model: str = "gpt-4o-mini") -> str:
    """
    Send a chat completion request and return the assistant message content.
    """
    client = _get_client()
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content
