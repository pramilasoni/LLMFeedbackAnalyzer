from pydantic import BaseModel
from typing import List
import json
from providers.llm_provider import generate_response


class AnalysisOutput(BaseModel):
    main_issues: List[str]
    severity: str
    evidence: List[str]
    recommended_focus: str


def generate_intermediate_analysis(question: str, intent: str, records: list):
    context = json.dumps(records, indent=2)

    messages = [
        {
            "role": "system",
            "content": """
Return ONLY valid JSON with:
{
  "main_issues": ["..."],
  "severity": "low | medium | high",
  "evidence": ["..."],
  "recommended_focus": "..."
}
"""
        },
        {
            "role": "user",
            "content": f"""
Intent: {intent}
Question: {question}
Data: {context}
"""
        }
    ]

    response = generate_response(messages)

    try:
        data = json.loads(response)
        validated = AnalysisOutput(**data)
        return validated.dict()
    except:
        # fallback if LLM fails
        return {
            "main_issues": [],
            "severity": "unknown",
            "evidence": [],
            "recommended_focus": "Unable to determine"
        }