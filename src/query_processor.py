import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def process_query(query: str) -> str:
    prompt = f"""
You are an expert HR analyst.
Extract the core skills, role, and intent from the query below.
Rewrite it as a concise search-friendly description.

Query:
{query}
"""
    response = model.generate_content(prompt)
    return response.text.strip()
