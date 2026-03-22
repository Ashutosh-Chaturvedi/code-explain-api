from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI
import sys
import json

load_dotenv(override=True)

app = FastAPI(title="Code Explain API")

class CodeRequest(BaseModel):
    code: str

@app.post("/explain")
def explain_code(request: CodeRequest):
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    response = client.responses.create(
        model="gpt-4o-mini",
        input=f"""
    You are a strict JSON generator.

    Return ONLY valid JSON. Do NOT include markdown, backticks, or explanations.

    Format:
    {{
    "summary": "...",
    "time_complexity": "...",
    "space_complexity": "...",
    "concepts": ["...", "..."],
    "improvements": "..."
    }}

    Code:
    {request.code}
    """,
        max_output_tokens=200
    )
    
    raw = response.output_text.strip()

    # remove markdown if still present
    if raw.startswith("```"):
        raw = raw.split("```")[1]  # remove ```json
        raw = raw.replace("json", "", 1).strip()

    import json

    try:
        analysis = json.loads(raw)
    except:
        analysis = {
            "summary": raw,
            "time_complexity": "N/A",
            "space_complexity": "N/A",
            "concepts": [],
            "improvements": "N/A"
        }
    
    return {
        "status": "success",
        "analysis": analysis
    }

@app.get("/")
def health():
    return {"status": "success", "service": "code-explain-api"}