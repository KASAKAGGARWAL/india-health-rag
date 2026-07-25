"""
retriever.py

Loads the FAISS index and performs semantic search.
"""

import pickle

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from config import (
    EMBEDDING_MODEL,
    FAISS_INDEX_PATH,
    CHUNKS_PATH,
    TOP_K_RESULTS,
)


class Retriever:
    def __init__(self):

        self.model = SentenceTransformer(EMBEDDING_MODEL)

        self.index = faiss.read_index(str(FAISS_INDEX_PATH))

        with open(CHUNKS_PATH, "rb") as f:
            self.chunks = pickle.load(f)

    def search(self, query, top_k=TOP_K_RESULTS):

        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        )

        distances, indices = self.index.search(
            np.asarray(query_embedding).astype("float32"),
            top_k,
        )

        results = []

        for score, idx in zip(distances[0], indices[0]):

            if idx == -1:
                continue

            chunk = self.chunks[idx]

            if isinstance(chunk, dict):
                text = chunk["text"]
                chunk_id = chunk["id"]
            else:
                text = chunk
                chunk_id = idx

            similarity = 1 / (1 + score)

            results.append(
                {
                    "id": chunk_id,
                    "text": text,
                    "score": round(similarity, 3),
                }
            )

        return results