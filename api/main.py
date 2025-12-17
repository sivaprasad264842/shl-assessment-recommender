from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.recommender import Recommender

app = FastAPI()
engine = Recommender()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/recommend")
def recommend(payload: dict):
    try:
        query = payload.get("query", "")
        recs = engine.recommend(query)

        return {
            "recommended_assessments": [
                {
                    "name": r["name"].strip(),
                    "url": r["url"].strip(),
                    "description": r["description"].strip(),
                    "test_type": [r["test_type"].strip()],
                    "duration": 90,
                    "remote_support": "Yes",
                    "adaptive_support": "No"
                }
                for r in recs
            ]
        }
    except Exception as e:
        return {"error": str(e)}

