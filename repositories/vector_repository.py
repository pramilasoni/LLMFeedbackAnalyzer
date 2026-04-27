import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="feedback_embeddings"
)


def save_feedback_vector(record: dict):
    record_id = record["customer_id"]

    document = (
        " ".join(record["topics"])
        + " "
        + record["sentiment"]
        + " "
        + record["priority"]
        + " "
        + record["recommended_action"]
    )

    collection.upsert(
        ids=[record_id],
        documents=[document],
        embeddings=[record["embedding"]],
        metadatas=[{
            "customer_id": record["customer_id"],
            "sentiment": record["sentiment"],
            "priority": record["priority"],
            "topics": ", ".join(record["topics"]),
            "recommended_action": record["recommended_action"]
        }]
    )


def search_similar_feedback(question_embedding, top_k=5):
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k
    )

    records = []

    for metadata, document in zip(
        results["metadatas"][0],
        results["documents"][0]
    ):
        records.append({
            "customer_id": metadata["customer_id"],
            "sentiment": metadata["sentiment"],
            "priority": metadata["priority"],
            "topics": metadata["topics"].split(", "),
            "recommended_action": metadata["recommended_action"],
            "document": document
        })

    return records