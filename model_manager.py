from sentence_transformers import SentenceTransformer

def get_model(name: str = "sentence-transformers/all-MiniLM-L6-v2") -> SentenceTransformer:
    try:
        return SentenceTransformer(name)
    except Exception as e:
        raise RuntimeError(f"Failed to load model '{name}': {e}")
