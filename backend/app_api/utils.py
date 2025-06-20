from sentence_transformers import SentenceTransformer, util
import pdfplumber 
import re


def extract_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"  
    return text.strip()


def preprocess(text):
    text = re.sub(r'\S+@\S+', ' ', text)        
    text = re.sub(r'http\S+', ' ', text)   
    text = text.lower()                          
    text = re.sub(r"[^a-z0-9,.()\-\n ]", " ", text)  
    text = re.sub(r'\s+', ' ', text)            
    return text.strip()

model = SentenceTransformer('all-MiniLM-L6-v2')
def compute_match_score(resume_text, job_description):
    resume_text = preprocess(resume_text)
    job_description = preprocess(job_description)
    embeddings = model.encode([resume_text, job_description], convert_to_tensor=True)
    score = util.cos_sim(embeddings[0], embeddings[1])
    return round(float(score) * 100, 2)  
