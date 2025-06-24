from data_loader import load_data
from text_processor import clean_text
from model_manager import get_model
from semantic_index import build_or_load_semantic_index
from keyword_index import build_keyword_index
from hybrid_searcher import run_hybrid_search

if __name__ == "__main__":
    df = load_data("data.csv")
    model = get_model()
    texts = [clean_text(row["TITLE"], row["DESCRIPTION"]) for _, row in df.iterrows()]
    _, index = build_or_load_semantic_index(texts, model)
    build_keyword_index(texts)

    while True:
        q = input("Search: ")
        results = run_hybrid_search(q, df, model, index)
        for r in results:
            print(f"\n🔍 {r['title']}\n📅 {r['date']} | 📰 {r['source']}\n📝 {r['summary']}\n")
