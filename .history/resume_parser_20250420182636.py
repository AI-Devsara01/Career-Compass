import os
import re
import spacy
import docx
import fitz  # PyMuPDF for extracting PDF text
import pytesseract
from pdf2image import convert_from_path
from collections import defaultdict
import language_tool_python

# Load SpaCy model and grammar checker
nlp = spacy.load("en_core_web_sm")
tool = language_tool_python.LanguageTool('en-US')

# Role keywords dictionary
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

# Learning resources for missing skills
SKILL_RESOURCES = {
    "machine learning": "https://www.coursera.org/learn/machine-learning",
    "deep learning": "https://www.deeplearning.ai/ai-for-everyone/",
    "tensorflow": "https://www.tensorflow.org/tutorials",
    "pytorch": "https://pytorch.org/tutorials/",
    "python": "https://www.learnpython.org/",
    "scikit-learn": "https://scikit-learn.org/stable/user_guide.html",
    "aws": "https://aws.amazon.com/training/",
    "azure": "https://learn.microsoft.com/en-us/azure/",
    "docker": "https://www.docker.com/101-tutorial/",
    # Add more as needed
}

# OCR fallback for scanned PDFs
def extract_text_with_ocr(pdf_path):
    try:
        images = convert_from_path(pdf_path)
        text = ""
        for img in images:
            text += pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"[ERROR] OCR failed: {e}")
        return ""

# Text extraction from PDF, DOCX, DOC
def extract_text(file_path):
    text = ""
    ext = os.path.splitext(file_path)[-1].lower()

    try:
        if ext == ".pdf":
            doc = fitz.open(file_path)
            for page_num in range(doc.page_count):
                page = doc.load_page(page_num)
                text += page.get_text("text")
            if not text.strip():
                print("[INFO] No text found with PyMuPDF. Trying OCR...")
                text = extract_text_with_ocr(file_path)

        elif ext in [".docx", ".doc"]:
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                text += para.text
        else:
            print(f"[WARN] Unsupported file type: {ext}")
    except Exception as e:
        print(f"[ERROR] Failed to extract text: {e}")

    print(f"\n[DEBUG] Extracted text (first 500 chars):\n{text[:500]}")
    return text.lower() if text else None

# Role recommendation logic
def recommend_role(resume_text):
    if not resume_text or not isinstance(resume_text, str) or not resume_text.strip():
        print("No text extracted from the resume!")
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

    # Grammar check
    grammar_matches = tool.check(resume_text)
    grammar_issues = [match.message for match in grammar_matches[:5]]  # Top 5 issues

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

# CLI runner
def main():
    file_path = input("Enter the path to the resume file (PDF, DOCX, DOC): ").strip()
    if not os.path.exists(file_path):
        print("[ERROR] File path does not exist!")
        return

    print("[INFO] Extracting text from the resume...")
    resume_text = extract_text(file_path)

    if resume_text:
        result = recommend_role(resume_text)
        print("\n===== Resume Analysis Report =====")
        print(f"Recommended Role: {result['recommended_role']}")
        print(f"ATS Score: {result['ats_score']}%")
        print(f"Matched Keywords: {result['matched_keywords']}")
        print(f"Missing Keywords: {result['missing_keywords']}")
        print(f"Recommended Resources: {result['recommendations']}")
        print(f"Grammar Issues (if any): {result['grammar_issues']}")
        print(f"Suggestions: {result['areas_of_improvement']}")
    else:
        print("[ERROR] No text extracted from the resume!")

