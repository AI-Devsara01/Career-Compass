import spacy
import os
import re
from PyPDF2 import PdfReader
import docx

# Load SpaCy model (can be useful later if you want to extract skills/nouns etc.)
nlp = spacy.load("en_core_web_sm")

# Define keywords for each role
ROLE_KEYWORDS = {
    "AI/ML Engineer": ["machine learning", "deep learning", "tensorflow", "pytorch", "AI", "ML"],
    "Data Scientist": ["data analysis", "python", "statistics", "pandas", "numpy", "visualization"],
    "Cloud Engineer": ["aws", "azure", "gcp", "cloud", "devops"],
    "Cybersecurity Analyst": ["cybersecurity", "network", "threat", "vulnerability", "security"],
    "Full Stack Developer": ["javascript", "react", "node", "backend", "frontend", "django", "flask"]
}

# Extract raw text from resume file
def extract_text(file_path):
    text = ""
    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".pdf":
        try:
            reader = PdfReader(file_path)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
        except Exception as e:
            print(f"[ERROR] PDF parsing failed: {e}")
    elif ext in [".docx", ".doc"]:
        try:
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                text += para.text
        except Exception as e:
            print(f"[ERROR] DOC parsing failed: {e}")
    else:
        print(f"[WARN] Unsupported file type: {ext}")

    return text.lower()

# Recommend a role based on extracted resume text
def recommend_role(resume_text):
    scores = {role: 0 for role in ROLE_KEYWORDS}

    for role, keywords in ROLE_KEYWORDS.items():
        for kw in keywords:
            pattern = r'\b' + re.escape(kw.lower()) + r'\b'
            if re.search(pattern, resume_text):
                scores[role] += 1

    # Debug print to see what matched
    print(f"[INFO] Role Scores: {scores}")

    best_match = max(scores, key=scores.get)
    if scores[best_match] == 0:
        return "ds"  # Default fallback role if no keyword matched

    ROLE_SLUGS = {
        "AI/ML Engineer": "ai_engineer",
        "Data Scientist": "ds",
        "Cloud Engineer": "cloud_engineer",
        "Cybersecurity Analyst": "cybersecurity_analyst",
        "Full Stack Developer": "full_stack"
    }

    return ROLE_SLUGS.get(best_match, "ds")
