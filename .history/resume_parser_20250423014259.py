import os
import re
import spacy
import docx
import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import cv2
from collections import defaultdict
import language_tool_python

# Load NLP model and grammar tool
nlp = spacy.load("en_core_web_sm")
tool = language_tool_python.LanguageTool('en-US')

# Set tesseract path (update if installed elsewhere)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Define role keywords
ROLE_KEYWORDS = {
    "AI Engineer": ["machine learning", "deep learning", "tensorflow", "pytorch", "AI", "ML", "scikit-learn", "model training", "neural networks"],
    "Data Scientist": ["data analysis", "python", "statistics", "pandas", "numpy", "visualization", "regression", "EDA", "data mining"],
    "Cloud Engineer": ["aws", "azure", "gcp", "cloud", "devops", "kubernetes", "docker", "infrastructure", "cloud computing"],
    "Cybersecurity Analyst": ["cybersecurity", "network", "threat", "vulnerability", "security", "encryption", "firewall", "penetration testing"],
    "Full Stack Developer": ["javascript", "react", "node", "backend", "frontend", "django", "flask", "express", "api", "database"],
    "DevOps Engineer": ["CI/CD", "jenkins", "docker", "kubernetes", "ansible", "terraform", "monitoring", "automation", "infrastructure"],
    "Software Engineer": ["java", "c++", "python", "algorithms", "system design", "oop", "data structures", "software development"],
    "Product Manager": ["agile", "roadmap", "stakeholders", "market research", "user stories", "product", "MVP", "product strategy"],
    "Blockchain Developer": ["blockchain", "ethereum", "solidity", "smart contract", "web3", "dapps", "crypto", "nft", "decentralized"],
    "UI/UX Designer": ["wireframes", "prototyping", "user research", "figma", "adobe xd", "interaction design", "usability", "ui", "ux"]
}

# Skill resource mapping
SKILL_RESOURCES = {
    "machine learning": "https://www.coursera.org/learn/machine-learning",
    "deep learning": "https://www.deeplearning.ai/ai-for-everyone/",
    "tensorflow": "https://www.tensorflow.org/tutorials",
    "pytorch": "https://pytorch.org/tutorials/",
    "python": "https://www.learnpython.org/",
    "scikit-learn": "https://scikit-learn.org/stable/user_guide.html",
    "aws": "https://aws.amazon.com/training/",
    "azure": "https://learn.microsoft.com/en-us/azure/",
    "docker": "https://www.docker.com/101-tutorial/"
}

# OCR for scanned PDFs
def extract_text_with_ocr(pdf_path):
    try:
        images = convert_from_path(pdf_path, dpi=300)
        if not images:
            print("[ERROR] No images were created from PDF")
            return ""
        text = ""
        for img in images:
            open_cv_image = np.array(img)
            gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            processed_img = Image.fromarray(thresh)
            text += pytesseract.image_to_string(processed_img, config="--psm 6")
        return text
    except Exception as e:
        print(f"[ERROR] OCR failed: {e}")
        return ""

# Unified text extraction for PDF/DOCX
def extract_text(file_path):
    text = ""
    ext = os.path.splitext(file_path)[-1].lower()

    try:
        if ext == ".pdf":
            doc = fitz.open(file_path)
            for page in doc:
                text += page.get_text("text")

            if not text.strip():
                print("[INFO] No text found with PyMuPDF. Trying OCR...")
                text = extract_text_with_ocr(file_path)
                print(f"[DEBUG] OCR Text Extracted:\n{text[:500]}")
        elif ext in [".docx", ".doc"]:
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                text += para.text
        else:
            print(f"[WARN] Unsupported file type: {ext}")
    except Exception as e:
        print(f"[ERROR] Failed to extract text: {e}")
        return None

    cleaned_text = text.replace('\n', ' ').replace('\r', ' ').strip()
    if cleaned_text:
        return (cleaned_text.lower(), recommend_role(cleaned_text.lower()))
    else:
        return None

# Role recommender engine
def recommend_role(resume_text):
    if not resume_text or not isinstance(resume_text, str) or not resume_text.strip():
        return {
            "role_slug": "",
            "recommended_role": "No suitable match",
            "ats_score": 0,
            "matched_keywords": [],
            "missing_keywords": [],
            "recommendations": {},
            "grammar_issues": [],
            "areas_of_improvement": ["Ensure your resume contains key skills and experience."]
        }

    scores = {role: 0 for role in ROLE_KEYWORDS}
    keyword_hits = {role: [] for role in ROLE_KEYWORDS}

    for role, keywords in ROLE_KEYWORDS.items():
        for kw in keywords:
            if re.search(r'\b' + re.escape(kw.lower()) + r'\b', resume_text):
                scores[role] += 1
                keyword_hits[role].append(kw)

    best_match = max(scores, key=scores.get)
    matched_keywords = keyword_hits[best_match]

    if scores[best_match] == 0:
        return {
            "role_slug": "",
            "recommended_role": "No suitable match",
            "ats_score": 0,
            "matched_keywords": [],
            "missing_keywords": [],
            "recommendations": {},
            "grammar_issues": [],
            "areas_of_improvement": ["Ensure your resume contains key skills and experience."]
        }

    total_keywords = ROLE_KEYWORDS[best_match]
    missing_keywords = list(set(total_keywords) - set(matched_keywords))
    ats_score = round((len(matched_keywords) / len(total_keywords)) * 100)

    recommendations = {
        skill: SKILL_RESOURCES.get(skill) for skill in missing_keywords if skill in SKILL_RESOURCES
    }

    grammar_matches = tool.check(resume_text)
    grammar_issues = [match.message for match in grammar_matches[:5]]

    return {
        "role_slug": best_match.lower().replace(" ", "_"),
        "recommended_role": best_match,
        "ats_score": ats_score,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "recommendations": recommendations,
        "grammar_issues": grammar_issues,
        "areas_of_improvement": ["Include more relevant keywords.", "Improve grammar if flagged."]
    }
