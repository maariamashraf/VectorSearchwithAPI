import os
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from bs4 import BeautifulSoup

# === 1. Load and clean the data ===
df = pd.read_csv("data.csv", dtype=str) #read csv file into data frame
df.fillna("", inplace=True) #fill null with empty char

# === 2. File paths for metadata ===
EMBEDDINGS_FILE = "embeddings.npy" #vector rep in file
INDEX_FILE = "faiss.index" #search index
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2" #calc the embedding values

# === 3. Load or create the FAISS index and embeddings ===
print("Checking for cached vector data...")
if os.path.exists(EMBEDDINGS_FILE) and os.path.exists(INDEX_FILE): #retreive from files
    print(" Loaded from cache.")
    embeddings = np.load(EMBEDDINGS_FILE)
    index = faiss.read_index(INDEX_FILE)
else:
    print(" Generating embeddings and FAISS index for the first time...")
    model = SentenceTransformer(MODEL_NAME)

    cleaned_texts = [
        BeautifulSoup(row["TITLE"] + " " + row["DESCRIPTION"], "html.parser").get_text(separator=" ") #combine then clean
        for _, row in df.iterrows()
    ]

    embeddings = model.encode(cleaned_texts, show_progress_bar=True).astype("float32")#convert embd. for faiss

    # Save the data for future runs
    np.save(EMBEDDINGS_FILE, embeddings)

    index = faiss.IndexFlatL2(embeddings.shape[1]) #save Euclidean distance of emdb.
    index.add(embeddings)
    faiss.write_index(index, INDEX_FILE)



def search(query, top_k=10):  # Top_k is higher to compensate for filtering duplicates
    model = SentenceTransformer(MODEL_NAME) #load model again
    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, top_k) #return values of searching in index file

    seen_titles = set() #empty set
    printed = 0
    print(f"\n Top {min(top_k, 5)} unique results for: \"{query}\"\n" + "-" * 60)

    for idx, dist in zip(indices[0], distances[0]):
        title = df.iloc[idx]["TITLE"].strip()

        # Skip duplicates
        if title in seen_titles:
            continue
        seen_titles.add(title)

        date = df.iloc[idx]["MOD_DATE"]
        source = df.iloc[idx]["SOURCE_NAME"]
        description = BeautifulSoup(df.iloc[idx]["DESCRIPTION"], "html.parser").get_text(separator=" ")
        short_summary = description.strip().replace("\n", " ")[:300]

        printed += 1
        print(f" Result #{printed}")
        print(f" Title   : {title}")
        print(f" Date    : {date} |  Source: {source}")
        print(f" Summary : {short_summary}...")
        print("-" * 60)

        if printed >= 5:
            break

    if printed == 0:
        print(" No unique results found.")


# === 5. Input from user ===
if __name__ == "__main__":
    user_query = input("\n Enter your search query: ")
    search(user_query)

