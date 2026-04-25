import numpy as np


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def get_top_k_similar(question_embedding, records, k=3):
    scored = []

    for item in records:
        if "embedding" in item:
            score = cosine_similarity(question_embedding, item["embedding"])
            scored.append((score, item))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [item for _, item in scored[:k]]