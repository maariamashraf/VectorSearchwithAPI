def build_or_load_semantic_index(texts, model, emb_file="embeddings.npy", index_file="faiss.index"):
    import faiss
    import numpy as np
    import os
    from file_manager import load_index, load_embeddings, save_embeddings, save_index

    if os.path.exists(emb_file) and os.path.exists(index_file):
        embeddings = load_embeddings(emb_file)
        index = load_index(index_file)
    else:
        embeddings = model.encode(texts, show_progress_bar=True).astype("float32")
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)
        save_embeddings(emb_file, embeddings)
        save_index(index_file, index)
    return embeddings, index
