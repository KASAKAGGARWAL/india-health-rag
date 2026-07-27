"""
Central configuration for the RAG application.
Keeping all configurable values in one place makes the project
easier to maintain and modify.
"""

from pathlib import Path

# -------------------------------
# Project Paths
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "data" / "pib_document.html"

VECTORSTORE_DIR = BASE_DIR / "vectorstore"

FAISS_INDEX_PATH = VECTORSTORE_DIR / "faiss.index"

CHUNKS_PATH = VECTORSTORE_DIR / "chunks.pkl"

# -------------------------------
# Embedding Model
# -------------------------------

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# -------------------------------
# Chunking
# -------------------------------

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# -------------------------------
# Retrieval
# -------------------------------

TOP_K_RESULTS = 5

# -------------------------------
# LLM
# -------------------------------

LLM_MODEL = "llama-3.1-8b-instant"

---
