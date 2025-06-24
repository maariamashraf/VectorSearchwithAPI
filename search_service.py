from hybrid_searcher import run_hybrid_search
from model_manager import get_model
from data_loader import load_data
from text_processor import clean_text
from semantic_index import build_or_load_semantic_index
from keyword_index import build_keyword_index

# Load and initialize at import
_df = load_data("data.csv")
_model = get_model()
_texts = [clean_text(row["TITLE"], row["DESCRIPTION"]) for _, row in _df.iterrows()]
_embeddings, _sem_index = build_or_load_semantic_index(_texts, _model)
build_keyword_index(_texts)

def perform_search(query: str) -> str:
    return run_hybrid_search(query, _df, _model, _sem_index)
