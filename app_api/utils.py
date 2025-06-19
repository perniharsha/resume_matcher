from sentence_transformers import SentenceTransformer, util
import pdfplumber 
import re

# --------------------- Extract text from PDF ---------------------
def extract_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"  # ✅ Fixed typo: extract_texct → extract_text
    return text.strip()

# --------------------- Preprocess text ---------------------
def preprocess(text):
    text = re.sub(r'\S+@\S+', ' ', text)         # Remove emails
    text = re.sub(r'http\S+', ' ', text)         # Remove URLs
    text = text.lower()                          # Lowercase
    text = re.sub(r"[^a-z0-9,.()\-\n ]", " ", text)  # ✅ Fix: proper regex to REMOVE unwanted chars
    text = re.sub(r'\s+', ' ', text)             # ✅ Fix: replace multiple spaces/newlines with one
    return text.strip()

# --------------------- Load model ---------------------
model = SentenceTransformer('all-MiniLM-L6-v2')

# --------------------- Compute similarity score ---------------------
def compute_match_score(resume_text, job_description):
    resume_text = preprocess(resume_text)
    job_description = preprocess(job_description)
    embeddings = model.encode([resume_text, job_description], convert_to_tensor=True)
    score = util.cos_sim(embeddings[0], embeddings[1])
    return round(float(score) * 100, 2)  # Return as percentage
