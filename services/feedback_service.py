import json

from providers.llm_provider import generate_response
from providers.embedding_provider import get_embedding
from repositories.data_repository import save_record


def analyze_feedback(customer_id: str, feedback: str):
    messages = [
        {
            "role": "system",
            "content": """
Return ONLY valid JSON. No explanation.

Format:
{
  "sentiment": "...",
  "topics": ["..."],
  "priority": "...",
  "recommended_action": "..."
}
"""
        },
        {
            "role": "user",
            "content": feedback
        }
    ]

    llm_output = generate_response(messages)

    result = json.loads(llm_output)

    result["customer_id"] = customer_id

    text_for_embedding = (
        " ".join(result["topics"])
        + " "
        + result["sentiment"]
        + " "
        + result["priority"]
        + " "
        + result["recommended_action"]
    )

    result["embedding"] = get_embedding(text_for_embedding)

    save_record(result)

    return result