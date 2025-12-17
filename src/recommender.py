import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

class Recommender:
    def __init__(self):
        # Load catalog
        if not os.path.exists("data/shl_catalog.csv"):
            raise FileNotFoundError("shl_catalog.csv missing")

        self.df = pd.read_csv("data/shl_catalog.csv")

        if self.df.empty:
            raise ValueError("shl_catalog.csv is EMPTY")

        
        self.df.columns = [c.strip().lower() for c in self.df.columns]

        
        column_aliases = {
            "test type": "test_type",
            "testtype": "test_type",
            "type": "test_type",
            "category": "test_type",
            "assessment_type": "test_type",
            "desc": "description",
            "details": "description",
        }

        self.df.rename(columns=column_aliases, inplace=True)

        # Validate required schema
        required_columns = {"name", "url", "description", "test_type"}
        missing = required_columns - set(self.df.columns)

        if missing:
            raise ValueError(f"Missing required columns in catalog: {missing}")

        # Load embeddings
        if not os.path.exists("embeddings/catalog_embeddings.npy"):
            raise FileNotFoundError("catalog_embeddings.npy missing. Run embedder.py")

        self.embeddings = np.load("embeddings/catalog_embeddings.npy")

        if len(self.df) != len(self.embeddings):
            raise ValueError("Catalog rows and embeddings count mismatch")

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def recommend(self, query, k=10):
        query_vec = self.model.encode([query])
        scores = cosine_similarity(query_vec, self.embeddings)[0]

        self.df["score"] = scores

        results = []

        # Balanced recommendation: K + P + C
        for t in ["k", "p", "c"]:
            subset = self.df[
                self.df["test_type"]
                .fillna("")
                .astype(str)
                .str.lower()
                == t
            ]   
            if not subset.empty:
                results.extend(
                    subset.sort_values("score", ascending=False)
                    .head(max(1, k // 3))
                    .to_dict("records")
                )

        # Fallback if balance is impossible
        if len(results) < k:
            results = (
                self.df.sort_values("score", ascending=False)
                .head(k)
                .to_dict("records")
            )

        return sorted(results, key=lambda x: x["score"], reverse=True)[:k]
