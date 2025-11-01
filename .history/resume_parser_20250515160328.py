from flask import Flask, render_template, request
import fitz  # PyMuPDF for PDF parsing
import re
import os
from werkzeug.utils import secure_filename

app = Flask(_name_)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Define role-specific keywords and action verbs
role_keywords = {
    'ai_engineer': ['machine learning', 'python', 'tensorflow', 'pandas', 'keras', 'deep learning', 'nlp'],
    'full_stack_developer': ['html', 'css', 'javascript', 'react', 'node.js', 'express', 'mongodb', 'frontend', 'backend'],
    'data_scientist': ['data analysis', 'python', 'matplotlib', 'statistics', 'sql', 'seaborn', 'data visualization'],
}

action_verbs = [
    'developed', 'implemented', 'analyzed', 'created', 'designed', 'led', 'built', 'managed', 'automated', 'optimized'
]

required_sections = ['education', 'experience', 'skills', 'projects']

# Utility: Extract text from uploaded PDF
def extract_text(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return " ".join([page.get_text() for page in doc])

# Utility: Check for required sections
def check_sections(text):
    found = []
    for section in required_sections:
        if section.lower() in text.lower():
            found.append(section)
    return found

# Utility: Check for action verbs
def find_action_verbs(text):
    found = []
    for verb in action_verbs:
        if re.search(rf'\b{verb}\b', text, re.IGNORECASE):
            found.append(verb)
    return list(set(found))

@app.route("/")
def home():
    return render_template("resume.html")

@app.route("/upload", methods=["POST"])
def upload():
    if 'resume' not in request.files:
        return "No resume file uploaded."

    resume_file = request.files['resume']
    role = request.form.get("role")

    if role not in role_keywords:
        return "Invalid role selected."

    resume_text = extract_text(resume_file)

    # Keyword Matching
    keywords = role_keywords[role]
    matched_keywords = [kw for kw in keywords if kw.lower() in resume_text.lower()]
    missing_keywords = list(set(keywords) - set(matched_keywords))

    # Section Check
    matched_sections = check_sections(resume_text)
    missing_sections = list(set(required_sections) - set(matched_sections))

    # Action Verbs
    matched_verbs = find_action_verbs(resume_text)

    # Scoring
    keyword_score = int((len(matched_keywords) / len(keywords)) * 60)
    section_score = int((len(matched_sections) / len(required_sections)) * 20)
    verb_score = int((len(matched_verbs) / len(action_verbs)) * 20)
    total_score = keyword_score + section_score + verb_score

    return render_template("result.html",
                           score=total_score,
                           matched=matched_keywords,
                           missing=missing_keywords,
                           matched_sections=matched_sections,
                           missing_sections=missing_sections,
                           matched_verbs=matched_verbs,
                           role=role.replace('_', ' ').title())