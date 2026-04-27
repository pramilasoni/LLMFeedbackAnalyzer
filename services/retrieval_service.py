from services.cache_service import get_question_embedding
from repositories.vector_repository import search_similar_feedback


def retrieve_feedback(query: str, top_k: int = 5):
    query_embedding = get_question_embedding(query)

    return search_similar_feedback(
        question_embedding=query_embedding,
        top_k=top_k
    )