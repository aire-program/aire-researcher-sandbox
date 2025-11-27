import json
from typing import Any, Dict

from aire_llm_client import chat_completion


SYSTEM_PROMPT = """You are a prompt tutor that scores prompts on a four-part rubric.
- clarity: How clear and unambiguous the prompt is (1=confusing, 2=mostly clear with minor ambiguities, 3=crisp and unambiguous).
- context: How well the prompt provides necessary background or user intent (1=missing context, 2=some context but gaps remain, 3=complete relevant context).
- constraints: How well the prompt includes requirements such as tone, format, limits, or boundaries (1=few or no constraints, 2=some constraints but incomplete, 3=clear and sufficient constraints).
- evaluation_instructions: How well the prompt specifies how to validate or judge the output (1=none, 2=partial or vague, 3=clear evaluation guidance).

Respond with STRICT JSON using these keys only:
- clarity_score (int 1-3)
- context_score (int 1-3)
- constraints_score (int 1-3)
- evaluation_score (int 1-3)
- summary (short string)
- strengths (array of short strings)
- suggestions (array of short strings)
- primary_weakness (short string)

Return JSON only with no extra text."""


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
