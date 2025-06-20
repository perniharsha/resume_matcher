# resume_matcher

# 🧠 Resume Matcher

An AI-powered Resume Matcher app that allows recruiters or HR professionals to upload job descriptions and candidate resumes, and receive matching scores using advanced Natural Language Processing techniques.

---

## 🚀 Features

- Upload resumes and job descriptions
- See similarity scores between resumes and job profiles
- Powered by modern ML models (Transformers, spaCy, etc.)
- Clean Streamlit frontend
- FastAPI backend


## 🛠️ Technologies Used

- 🧠 **FastAPI** — Backend API
- 📊 **Streamlit** — Frontend UI
- 🤖 **Transformers** (BERT) — Semantic similarity
- 🐍 Python 3.10+

---

## 🧪 Running Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/resume_matcher.git
cd resume_matcher
```
### 2️⃣ Start the Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate       
pip install -r requirements.txt
uvicorn app_api.main:app --host 0.0.0.0 --port 8000
```
### 3️⃣ Start the Frontend
```bash
cd frontend
python -m venv venv
venv\Scripts\activate        
pip install -r requirements.txt
streamlit run front_end/app.py
```

### 🌐 Deployment
Currently local only due to resource limits. Can be containerized and deployed using:
Docker 
Render, Railway, or any cloud service with GPU/CPU support
Separate backend and frontend services for scalability


### 📂 TODO
Add database for resume/job history

### 👤 Author
Sri HarshaVardhan Perni — GitHub

# 🧠 Resume Matcher

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-🚀-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-orange)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
