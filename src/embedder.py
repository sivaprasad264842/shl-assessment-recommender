import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import os

CATALOG_PATH = "data/shl_catalog.csv"
EMB_PATH = "embeddings/catalog_embeddings.npy"

if not os.path.exists(CATALOG_PATH):
    raise FileNotFoundError("shl_catalog.csv missing")

df = pd.read_csv(CATALOG_PATH)

if df.empty:
    raise ValueError("shl_catalog.csv is EMPTY")

# Normalize column names
df.columns = [c.strip().lower() for c in df.columns]

REQUIRED_COLUMNS = {"name", "url", "description", "test_type"}
missing = REQUIRED_COLUMNS - set(df.columns)

if missing:
    raise ValueError(f"Missing required columns: {missing}")

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(
    df["description"].astype(str).tolist(),
    show_progress_bar=True
)

os.makedirs("embeddings", exist_ok=True)
np.save(EMB_PATH, embeddings)

print("Embeddings created successfully:", embeddings.shape)
