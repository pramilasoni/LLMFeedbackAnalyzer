import json
from providers.llm_provider import generate_response


def detect_intent(question: str):
    messages = [
        {
            "role": "system",
            "content": """
Classify the user's question into one of the following intents:

- summary
- complaints
- sentiment
- recommendation
- trend

Return ONLY JSON:

{
  "intent": "..."
}
"""
        },
        {
            "role": "user",
            "content": question
        }
    ]

    response = generate_response(messages)

    try:
        result = json.loads(response)
        return result.get("intent", "summary")
    except:
        return "summary"