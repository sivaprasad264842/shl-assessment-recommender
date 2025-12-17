

# SHL Assessment Recommendation System (GenAI)

This project implements a **semantic, AI-powered recommendation system** that suggests relevant **SHL assessments** based on natural language job descriptions or hiring queries.

The system is built as part of the **SHL GenAI Intern Assignment** and follows the requirements outlined in the assignment document.

---

## What This Project Does

* Accepts a **free-text job description or hiring query**
* Understands required skills, role context, and constraints (time, seniority)
* Recommends relevant **SHL assessments**
* Ensures a **balanced mix** of:

  * Knowledge (K)
  * Personality (P)
  * Cognitive (C) tests
* Provides results via:

  * REST API (FastAPI)
  * Simple web frontend
  * CSV output for evaluation

---

## Key Technologies

* **Python**
* **FastAPI** – REST API
* **Sentence Transformers** – semantic embeddings
* **Cosine Similarity** – retrieval-based recommendation
* **Pandas / NumPy** – data processing
* **HTML + JavaScript** – frontend

---

## Project Highlights

* Semantic search instead of keyword matching
* Evaluation using **Recall@10**
* Uses **official SHL datasets** (train & test)
* End-to-end system: data → model → API → UI → predictions
* Production-style API with `/health` and `/recommend` endpoints

---

## Repository Structure (High Level)

```
api/        → FastAPI backend
src/        → Recommendation, evaluation, embeddings
data/       → SHL datasets and catalog
frontend/   → Web UI
outputs/    → predictions.csv
```

---

## How to Test Quickly

### API

```bash
uvicorn api.main:app --reload
```

Test:

```
POST /recommend
```

### Frontend

Open `frontend/index.html` in a browser and submit a job description.

---

## Submission Artifacts

* GitHub repository (this repo)
* Deployed API URL
* Deployed frontend URL
* `outputs/predictions.csv`
* `APPROACH.md` (design & methodology)

---

## Author

**Shiva**
Submission for **SHL GenAI Intern – Assessment Recommendation Engine**

---

### Final advice (listen carefully)

* This README is **perfect for GitHub**
* Your **detailed explanation belongs in APPROACH.md**, not here
* Do **not** over-edit this
* Commit, push, move on

If you want, I can also:

* Shorten this even more (ultra-minimal)
* Rewrite it in **SHL corporate tone**
* Check if your repo looks reviewer-ready at first glance
