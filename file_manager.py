import numpy as np
import os
import faiss

def save_embeddings(path: str, embeddings: np.ndarray):
    np.save(path, embeddings)

def load_embeddings(path: str) -> np.ndarray:
    return np.load(path)

def save_index(path: str, index):
    faiss.write_index(index, path)

def load_index(path: str):
    return faiss.read_index(path)
