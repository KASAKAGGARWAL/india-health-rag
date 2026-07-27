import os
import pickle

import faiss
import numpy as np
from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

from config import (
    DATA_PATH,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    FAISS_INDEX_PATH,
    CHUNKS_PATH,
)

def load_document(path: str) -> str:
    """
    Reads the HTML document and extracts clean text.
    """

    with open(path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")

    text = soup.get_text(separator="\n", strip=True)

    return text

def split_text(text: str):
    """
    Split the document into overlapping chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""]
    )

    chunks = splitter.split_text(text)

    return chunks

def load_embedding_model():
    """
    Load the sentence transformer model.
    """

    print("Loading embedding model...")

    model = SentenceTransformer(EMBEDDING_MODEL)

    print("Model loaded successfully!")

    return model

def create_embeddings(model, chunks):
    """
    Generate embeddings for all chunks.
    """

    print(f"Generating embeddings for {len(chunks)} chunks...")

    embeddings = model.encode(
        chunks,
        show_progress_bar=True,
        convert_to_numpy=True
    )

    print("Embeddings created!")

    return embeddings

def build_faiss_index(embeddings):
    """
    Build and save a FAISS index.
    """

    print("Building FAISS index...")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings.astype("float32"))

    faiss.write_index(index, str(FAISS_INDEX_PATH))

    print(f"FAISS index saved to {FAISS_INDEX_PATH}")

    return index

def save_chunks(chunks):
    """
    Save text chunks to disk.
    """

    with open(str(CHUNKS_PATH), "wb") as f:
        pickle.dump(chunks, f)

    print(f"Saved {len(chunks)} chunks.")


if __name__ == "__main__":

    text = load_document(DATA_PATH)

    chunks = split_text(text)

    print(f"Total Chunks: {len(chunks)}")

    model = load_embedding_model()

    embeddings = create_embeddings(model, chunks)

    print("Embedding Shape:", embeddings.shape)

    build_faiss_index(embeddings)

    save_chunks(chunks)

    print("\nDocument ingestion completed successfully!")
