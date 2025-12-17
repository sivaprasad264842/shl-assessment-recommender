import json
import csv
from recommender import Recommender
import os

engine = Recommender()

with open("data/test.json") as f:
    test = json.load(f)["Test-Set"]

os.makedirs("outputs", exist_ok=True)

with open("outputs/predictions.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Query", "Assessment_url"])

    for item in test:
        recs = engine.recommend(item["Query"])
        for r in recs:
            writer.writerow([item["Query"], r["url"]])

print("predictions.csv created")
