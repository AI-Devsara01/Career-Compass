import spacy
import os
import re
from PyPDF2 import PdfReader
import docx
from collections import defaultdict
import language_tool_python

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")
tool = language_tool_python.LanguageTool('en-US')

SECTION_WEIGHTS = {
    "education": 20,
    "experience": 30,
    "skills": 25,
    "projects": 15,
    "certifications": 10
}

SECTION_HEADERS = SECTION_WEIGHTS.keys()

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

def grade_sections(resume_text):
    section_scores = {}
    for section in SECTION_HEADERS:
        pattern = re.compile(rf"{section}", re.IGNORECASE)
        if pattern.search(resume_text):
            section_scores[section] = SECTION_WEIGHTS[section]
        else:
            section_scores[section] = 0
    total_score = sum(section_scores.values())
    return section_scores, total_score

def grammar_issues(resume_text):
    matches = tool.check(resume_text)
    return [{
        "message": m.message,
        "sentence": m.context.strip(),
        "offset": m.offset
    } for m in matches]

def recommend_role(resume_text):
    scores = {role: 0 for role in ROLE_KEYWORDS}
    keyword_hits = {role: [] for role in ROLE_KEYWORDS}

    for role, keywords in ROLE_KEYWORDS.items():
        for kw in keywords:
            pattern = r'\\b' + re.escape(kw.lower()) + r'\\b'
            if re.search(pattern, resume_text):
                scores[role] += 1
                keyword_hits[role].append(kw)

    best_match = max(scores, key=scores.get)
    if scores[best_match] == 0:
        return {
            "role_slug": "ds",
            "ats_score": 0,
            "matched_keywords": [],
            "missing_keywords": [],
            "recommendations": {},
            "section_scores": {},
            "grammar_issues": []
        }

    matched_keywords = keyword_hits[best_match]
    total_keywords = ROLE_KEYWORDS[best_match]
    missing_keywords = list(set(total_keywords) - set(matched_keywords))

    ats_score = round((len(matched_keywords) / len(total_keywords)) * 100)

    recommendations = {skill: SKILL_RESOURCES[skill] for skill in missing_keywords if skill in SKILL_RESOURCES}

    section_scores, section_total = grade_sections(resume_text)
    grammar_feedback = grammar_issues(resume_text)

    return {
        "role_slug": ROLE_SLUGS.get(best_match, "ds"),
        "ats_score": ats_score,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "recommendations": recommendations,
        "section_scores": section_scores,
        "section_total": section_total,
        "grammar_issues": grammar_feedback
    }

# Example usage:
# resume_text = extract_text("/path/to/resume.pdf")
# analysis = recommend_role(resume_text)
# print(analysis)
