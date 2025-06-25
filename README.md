# Vector Search with API

-----

## 🔍 **Hybrid Search Engine for Egyptian Financial News**

A fast and intelligent search system for financial news built with **Sentence Transformers**, **FAISS**, **keyword search (TF-IDF)**, and **FastAPI** — with both CLI and API interfaces.

-----

## 🚀 **Features**

  * ✅ **Hybrid Search**: Semantic (vector) + Keyword (TF-IDF)
  * 🇪🇬 **Optimized for Arabic-English financial news** (e.g., EGX, COMI.CA)
  * 🔎 **Smart Query Analysis**: Dynamically switches between search strategies
  * 🧠 **SentenceTransformer-backed embeddings** (MiniLM / MPNet)
  * ⚡ **Fast API & interactive CLI**
  * 🔧 **Modular & production-ready architecture**

-----

## 🧱 **System Architecture**

### 📂 **Core Files**

| Module              | Responsibility                 |
| :------------------ | :----------------------------- |
| `data_loader.py`    | CSV loading & validation       |
| `text_processor.py` | HTML cleaning, text normalization |
| `model_manager.py`  | Loads SentenceTransformer model |
| `file_manager.py`   | Caching for embeddings/index   |
| `semantic_index.py` | FAISS vector indexing          |
| `keyword_index.py`  | TF-IDF keyword indexing        |
| `query_analyzer.py` | Detects query type (short vs long) |
| `hybrid_searcher.py`| Combines results from both methods |
| `result_formatter.py`| Formats output text            |
| `main.py`           | CLI interface                  |

### 🌐 **API Files**

| File            | Role         |
| :-------------- | :----------- |
| `api_models.py` | Pydantic models |
| `search_service.py`| API logic    |
| `api_routes.py` | FastAPI routes |
| `api_server.py` | FastAPI app  |
| `run_api.py`    | API runner script |

-----

## ⚙️ **How It Works**

### 🧹 **Data Loading & Cleaning**

  * Loads `data.csv` using **pandas**
  * Cleans HTML using **BeautifulSoup**
  * Emphasizes titles for better short-query relevance

### 🧠 **Embedding Generation**

  * Uses model: `sentence-transformers/all-MiniLM-L6-v2`
  * Generates **384-dimension embeddings**
  * Saved locally in `.npy` format for reuse

### 🔎 **Semantic Search with FAISS**

  * Builds `IndexFlatL2` for vector similarity
  * Cached to `faiss.index`
  * Optimized for **long queries**

### 🧾 **Keyword Search with TF-IDF**

  * Uses n-gram **TF-IDF vectors** (scikit-learn)
  * Optimized for fast sparse matrix matching
  * Best for **short keywords** (e.g., "COMI", "CIB")

### 🤖 **Hybrid Search Engine**

  * **Short query** → Keyword search
  * **Long query** → Semantic search
  * Results are merged and deduplicated
  * **Top 5 relevant documents** shown

-----

## 💡 **CLI Usage**

To use the Command Line Interface:

```bash
python main.py
```

**Example:**

```bash
Enter your search query: comi

Top 5 results for: "comi"
------------------------------------------------------------
 Result #1
 Title   : Release from Commercial International Bank (CIB)
 Date    : 2025-06-03 | Source: MIST english news
 Summary : Company Name: Commercial International Bank (CIB) ...
------------------------------------------------------------
```

-----

## 🌐 **API Usage**

### ✅ **Start the server**

```bash
python run_api.py
```

Server starts at: `http://localhost:8000`

### 🚀 **Example request (GET)**

You can send a search query using a simple GET request with the query embedded in the URL path.

```bash
curl http://localhost:8000/search/comi

```

**Response:**

```json
{
  "results": [
    {
      "title": "Release from Commercial International Bank...",
      "summary": "...",
      "source": "MIST",
      "date": "2025-06-03"
    },
    ...
  ]
}
```

-----

## ✅ **Installation & Setup**

1.  **Create virtual environment**

    ```bash
    python -m venv .venv
    ```

2.  **Activate venv**

      * **Windows:**
        ```bash
        .venv\Scripts\activate
        ```
      * **Linux/macOS:**
        ```bash
        source .venv/bin/activate
        ```

3.  **Install requirements**

    ```bash
    pip install -r requirements.txt
    ```

### 📦 **Requirements Summary**

  * `pandas>=2.0.0`
  * `numpy>=1.24.0`
  * `faiss-cpu>=1.7.4`
  * `sentence-transformers>=2.2.0`
  * `scikit-learn>=1.3.0`
  * `beautifulsoup4>=4.12.0`
  * `scipy>=1.10.0`
  * `torch>=2.0.0`
  * `transformers>=4.30.0`
  * `requests>=2.28.0`
  * `urllib3>=1.26.0`
  * `fastapi>=0.100.0`
  * `uvicorn>=0.22.0`
  * `pydantic>=1.10.0`
