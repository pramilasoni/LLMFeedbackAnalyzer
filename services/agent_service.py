import json

from providers.llm_provider import generate_response
from services.retrieval_service import retrieve_feedback
from services.filtering_service import filter_complaints, filter_high_priority
from services.analysis_service import generate_intermediate_analysis


def plan_steps(question: str):
    messages = [
        {
            "role": "system",
            "content": """
You are an AI planner.

Break the user's request into steps using only these tools:

1. retrieve_feedback
- Purpose: search stored customer feedback using semantic search.
- Input: a short search query, such as "food quality complaints", "bathroom shower issues", or "customer dissatisfaction".
- Output: relevant feedback records.

2. filter_complaints
- Purpose: keep only negative or mixed feedback.
- Input: no text input needed. It works on the records from previous step.

3. filter_high_priority
- Purpose: keep only high-priority records.
- Input: no text input needed. It works on the records from previous step.

4. analyze
- Purpose: create structured analysis from the selected records.
- Input: no text input needed. It works on the current records.

5. summarize
- Purpose: generate final business answer from the analysis.
- Input: no text input needed.

Rules:
- Always start with retrieve_feedback.
- Use short, focused input for retrieve_feedback.
- Use filters only when they help the user request.
- End with summarize.

Return ONLY JSON:

{
  "steps": [
    {"tool": "...", "input": "..."}
  ]
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
        return json.loads(response)["steps"]
    except Exception:
        return [
            {"tool": "retrieve_feedback", "input": question},
            {"tool": "analyze", "input": ""},
            {"tool": "summarize", "input": ""}
        ]


def run_agent(question: str):
    steps = plan_steps(question)

    records = []
    analysis = None
    final_answer = None

    for step in steps:
        tool = step.get("tool")
        tool_input = step.get("input", "")

        if tool == "retrieve_feedback":
            query = tool_input if tool_input else question
            records = retrieve_feedback(query=query, top_k=5)

        elif tool == "filter_complaints":
            records = filter_complaints(records)

        elif tool == "filter_high_priority":
            records = filter_high_priority(records)

        elif tool == "analyze":
            analysis = generate_intermediate_analysis(
                question=question,
                intent="agent_investigation",
                records=records
            )

        elif tool == "summarize":
            if analysis is None:
                analysis = generate_intermediate_analysis(
                    question=question,
                    intent="agent_investigation",
                    records=records
                )

            messages = [
                {
                    "role": "system",
                    "content": """
You are an AI customer insights agent.

Use ONLY the provided analysis.
Provide:
- concise summary
- key issues
- recommended next actions
"""
                },
                {
                    "role": "user",
                    "content": f"""
Question:
{question}

Analysis:
{json.dumps(analysis, indent=2)}
"""
                }
            ]

            final_answer = generate_response(messages)

    if final_answer:
        return {
            "plan": steps,
            "answer": final_answer
        }

    return {
        "plan": steps,
        "answer": "Agent could not complete the request."
    }