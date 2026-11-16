# 🗄️ Python Vector Database with ChromaDB

A modular, hands-on Python project demonstrating core vector database concepts using **ChromaDB**. This repository covers local disk persistence, CRUD operations, metadata filtering (`$and`), vector embedding extraction, cosine similarity math, and semantic search using local ONNX embeddings (`all-MiniLM-L6-v2`).

---

## 🌟 Key Features

- **Persistent Storage (`PersistentClient`):** Saves vector collections locally to disk (`./chroma_db`) so embeddings persist across sessions.
- **Full CRUD Lifecycle:** Demonstrates creating collections, upserting/adding documents, reading records, and updating existing vectors.
- **Advanced Metadata Filtering:** Uses ChromaDB's `where` clause and `$and` logical operators to filter queries by structured attributes.
- **Embedding Inspection & Cosine Similarity:** Explicitly extracts raw high-dimensional vector embeddings (`include=["embeddings"]`) and compares vectors mathematically.
- **Semantic Search:** Performs concept-based similarity searches over compact, keyword-dense documents without relying on exact keyword matching.

---

## Demo



---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.10+
- **Vector Database:** ChromaDB (`chromadb`)
- **Embedding Model:** Default Local ONNX Runtime (`all-MiniLM-L6-v2`)
- **Environment Management:** Python `venv`, `python-dotenv`

---

## 📁 Project Structure

```text
python-vectordb-chromadb/
├── .venv/                      # Isolated Python virtual environment (git-ignored)
├── apps/                       # Application modules directory
├── notebooks/                  # Core vector database scripts & local storage
│   ├── chroma_db/              # Local SQLite & vector index storage (git-ignored)
│   ├── crud_operations.py      # Create, Read, Upsert, and Update vector operations
│   ├── embeddings_query.py     # Extracting raw vector embeddings & cosine similarity
│   ├── metadatas_query.py      # Filtering records using single & $and metadata rules
│   ├── persistent_client.py    # Connecting to and reading from persistent disk storage
│   ├── query.py                # Basic collection creation and similarity querying
│   └── semantic_search.py      # Context-driven semantic search implementation
├── .env                        # Local environment variables (git-ignored)
├── .gitignore                  # Excludes .venv, .env, __pycache__, and local DB files
├── README.md                   # Complete project documentation
└── requirement.txt             # Project dependencies
```

---

## ⚙️ Getting Started & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/chanchal-kumar-mandal/python-vectordb-chromadb.git
cd python-vectordb-chromadb
```

### 2. Create & Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirement.txt
```

---

## 🚀 Usage & Execution

Navigate into the `notebooks/` directory and run any of the modular scripts:

```bash
cd notebooks

# 1. Basic query and collection setup
python query.py

# 2. Verify persistent disk retrieval
python persistent_client.py

# 3. Run CRUD operations (Upsert & Update)
python crud_operations.py

# 4. Test single and $and metadata filtering
python metadatas_query.py

# 5. Inspect raw embedding vectors
python embeddings_query.py

# 6. Execute semantic search
python semantic_search.py
```

> **Note on First Run:** ChromaDB will automatically download the lightweight `all-MiniLM-L6-v2` ONNX embedding model (~79 MB) to your local user cache (`~/.cache/chroma/`). Subsequent runs execute completely offline and instantaneously.

---

## 🛡️ Best Practices & Troubleshooting

- **Exclude Local Vector Storage from Git:** Add `chroma_db/` (or `**/chroma_db/`) to your `.gitignore` file so binary SQLite files and local embeddings are not pushed to GitHub.
- **Explicit Embedding Inclusion:** By default, `collection.get()` returns `None` for embeddings to save memory. Always pass `include=["embeddings", "documents"]` when inspecting vectors.
- **Compound Filters:** When filtering on multiple metadata fields simultaneously in ChromaDB, wrap conditions inside an explicit `{"$and": [...]}` operator.