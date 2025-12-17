import json
from recommender import Recommender

def recall_at_k(actual, predicted, k=10):
    return len(set(actual) & set(predicted[:k])) / len(actual)

engine = Recommender()

with open("data/train.json") as f:
    train = json.load(f)["Train-Set"]

scores = []

for row in train:
    recs = engine.recommend(row["Query"])
    pred_urls = [r["url"] for r in recs]
    scores.append(recall_at_k([row["Assessment_url"]], pred_urls))

print("Mean Recall@10:", sum(scores) / len(scores))
