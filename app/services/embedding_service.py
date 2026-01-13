import json

import numpy as np
from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def generate(self, text: str) -> str:
        vector = self.model.encode(text)
        return json.dumps(vector.tolist())

    def similarity(self, emb1: str, emb2: str) -> float:
        v1 = np.array(json.loads(emb1))
        v2 = np.array(json.loads(emb2))
        return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
