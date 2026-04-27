from providers.embedding_provider import get_embedding
from utils.similarity import cosine_similarity

cache = []
embedding_cache = {}

SIMILARITY_THRESHOLD = 0.90


def normalize_question(question: str):
    return question.lower().strip()


def get_question_embedding(question: str):
    key = normalize_question(question)

    if key in embedding_cache:
        print("⚡ Embedding cache hit")
        return embedding_cache[key]

    embedding = get_embedding(question)
    embedding_cache[key] = embedding

    return embedding


def get_cached_answer(question: str):
    question_embedding = get_question_embedding(question)

    for item in cache:
        score = cosine_similarity(question_embedding, item["embedding"])

        if score >= SIMILARITY_THRESHOLD:
            print(f"⚡ Semantic cache hit: {score}")
            return item["answer"]

    return None


def save_cached_answer(question: str, answer: str):
    question_embedding = get_question_embedding(question)

    cache.append({
        "question": question,
        "embedding": question_embedding,
        "answer": answer
    })