from providers.llm_provider import generate_response
from services.cache_service import get_cached_answer, save_cached_answer
from services.intent_service import detect_intent
from services.retrieval_service import retrieve_feedback
from services.filtering_service import apply_intent_filter
from services.analysis_service import generate_intermediate_analysis


def ask_question(question: str):
    cached = get_cached_answer(question)
    if cached:
        return cached

    intent = detect_intent(question)

    records = retrieve_feedback(query=question, top_k=5)

    if not records:
        return "No relevant data found."

    filtered = apply_intent_filter(records, intent)

    if not filtered:
        return "No relevant data found for this question."

    analysis = generate_intermediate_analysis(
        question=question,
        intent=intent,
        records=filtered
    )

    messages = [
        {
            "role": "system",
            "content": """
You are an assistant generating business insights.

Rules:
- Use ONLY the provided analysis
- Do NOT add new information
- If data is insufficient, say so clearly
"""
        },
        {
            "role": "user",
            "content": f"""
Question:
{question}

Analysis:
{analysis}
"""
        }
    ]

    answer = generate_response(messages)

    save_cached_answer(question, answer)

    return answer