from query_analyzer import is_short_query
from keyword_index import search_keyword_index
from result_formatter import format_results

def run_hybrid_search(query, df, model, semantic_index):
    if is_short_query(query):
        indices = search_keyword_index(query)
    else:
        embedding = model.encode([query]).astype("float32")
        _, indices = semantic_index.search(embedding, 25)
        indices = indices[0]
    return format_results(indices, df)
