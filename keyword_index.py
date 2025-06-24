from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

_vectorizer = None
_matrix = None

def build_keyword_index(texts):
    global _vectorizer, _matrix
    _vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    _matrix = _vectorizer.fit_transform(texts)

def search_keyword_index(query: str, top_k=10):
    global _vectorizer, _matrix
    query_vec = _vectorizer.transform([query])
    scores = cosine_similarity(query_vec, _matrix).flatten()
    return scores.argsort()[::-1][:top_k]
