# main.py

from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import JSONResponse
from app_api.utils import extract_text, compute_match_score
import tempfile

app = FastAPI()

@app.post("/match")
async def match_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        content = await resume.read()
        tmp.write(content)
        tmp_path = tmp.name

    # Extract and compute score
    try:
        resume_text = extract_text(tmp_path)
        score = compute_match_score(resume_text, job_description)
        return JSONResponse({"match_score": score})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
