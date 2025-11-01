import spacy
import os
import re
from PyPDF2 import PdfReader
import docx
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

# Skill resources
SKILL_RESOURCES = {
    "tensorflow": "https://www.tensorflow.org/tutorials",
    "pytorch": "https://pytorch.org/tutorials/",
    "scikit-learn": "https://scikit-learn.org/stable/tutorial/index.html",
    "aws": "https://aws.amazon.com/training/",
    "docker": "https://docker-curriculum.com/",
    "kubernetes": "https://kubernetes.io/docs/tutorials/",
    "figma": "https://help.figma.com/hc/en-us/articles/360040514253-Learn-design-with-Figma",
    "solidity": "https://soliditylang.org/docs/",
    "system design": "https://github.com/donnemartin/system-design-primer",
    "oop": "https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-1-class-and-its-members/",
    "product strategy": "https://www.atlassian.com/product-management/strategy"
}

# Role slugs for cleaner naming (optional usage)
ROLE_SLUGS = {
    "AI Engineer": "ai_engineer",
    "Data Scientist": "data_scientist",
    "Cloud Engineer": "cloud_engineer",
    "Cybersecurity Analyst": "cybersecurity_analyst",
    "Full Stack Developer": "full_stack",
    "DevOps Engineer": "devops",
    "Software Engineer": "software_engineer",
    "Product Manager": "product_manager",
    "Blockchain Developer": "blockchain_dev",
    "UI/UX Designer": "uiux"
}

# Section weights for scoring
SECTION_WEIGHTS = {
    "education": 20,
    "experience": 30,
    "skills": 25,
    "projects": 15,
    "certifications": 10
}

# Extract text from resume file
def extract_text(file_path):
    text = ""
    ext = os.path.splitext(file_path)[-1].lower()

    try:
        if ext == ".pdf":
            reader = PdfReader(file_path)
            for page in reader.pages:
                if page.extract_text():
                    text += page.extract_text()
        elif ext in [".docx", ".doc"]:
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                text += para.text
        else:
            print(f"[WARN] Unsupported file type: {ext}")
    except Exception as e:
        print(f"[ERROR] Failed to extract text: {e}")
    
    return text.lower()

# Grade the structure of the resume based on key sections
def grade_sections(resume_text):
    section_scores = {}
    for section, weight in SECTION_WEIGHTS.items():
        pattern = re.compile(rf"\b{re.escape(section)}\b", re.IGNORECASE)
        section_scores[section] = weight if pattern.search(resume_text) else 0
    total_score = sum(section_scores.values())
    return section_scores, total_score

# Find grammar issues
def grammar_issues(resume_text):
    matches = tool.check(resume_text)
    return [{
        "message": m.message,
        "sentence": m.context.strip(),
        "offset": m.offset
    } for m in matches]
