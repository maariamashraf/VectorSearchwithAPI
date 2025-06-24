def is_short_query(query: str) -> bool:
    return len(query.strip().split()) <= 2

