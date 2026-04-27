import json

from providers.llm_provider import generate_response
from providers.embedding_provider import get_embedding
from repositories.data_repository import get_all_records
from utils.similarity import get_top_k_similar


def ask_question(question: str):
    records = get_all_records()

    if not records:
        return "No data available yet."

    question_embedding = get_embedding(question)

    top_results = get_top_k_similar(
        question_embedding=question_embedding,
        records=records,
        k=3
    )

    context = json.dumps(top_results, indent=2)

    messages = [
        {
            "role": "system",
            "content": "Answer ONLY based on the provided data. Do not make up information."
        },
        {
            "role": "user",
            "content": f"""
Data:
{context}

Question:
{question}
"""
        }
    ]

    return generate_response(messages)