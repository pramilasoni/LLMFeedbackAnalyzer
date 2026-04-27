def filter_complaints(records: list):
    return [
        r for r in records
        if r.get("sentiment") in ["negative", "mixed"]
    ]


def filter_high_priority(records: list):
    return [
        r for r in records
        if r.get("priority") == "high"
    ]


def apply_intent_filter(records: list, intent: str):
    if intent == "complaints":
        return filter_complaints(records)

    if intent == "recommendation":
        return filter_high_priority(records)

    if intent in ["summary", "sentiment", "trend"]:
        return records

    return records