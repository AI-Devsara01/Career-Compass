import numpy as np
import fitz  # PyMuPDF
import docx2txt
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import nltk
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Download required NLTK data
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

# ========== ENHANCED TECH ROLES WITH SKILL VARIATIONS ==========
TECH_ROLES = {
    "AI/ML Engineer": {
        "skills": ["machine learning", "deep learning", "neural networks", "tensorflow", 
                 "pytorch", "natural language processing", "computer vision", "artificial intelligence",
                 "scikit-learn", "opencv", "transformer models", "reinforcement learning", 
                 "model deployment", "keras", "llms", "generative ai"],
        "keywords": ["ml", "ai", "cnn", "rnn", "lstm", "bert", "gpu", "classification",
                   "random forest", "xgboost", "pipeline", "feature engineering"],
        "certifications": ["TensorFlow Developer", "AWS Certified Machine Learning", "Google Professional ML Engineer"]
    },
    "Data Scientist": {
        "skills": ["data analysis", "data visualization", "statistical modeling", "python", "r", 
                 "sql", "pandas", "numpy", "matplotlib", "seaborn", "scipy", "hypothesis testing",
                 "regression", "classification", "clustering", "time series", "experiment design"],
        "keywords": ["eda", "feature selection", "a/b testing", "power bi", "tableau",
                   "pyspark", "hadoop", "big data", "data mining", "predictive modeling"],
        "certifications": ["Microsoft Certified: Data Scientist", "Google Data Analytics", "IBM Data Science"]
    },
    "Cybersecurity Analyst": {
        "skills": ["network security", "ethical hacking", "incident response", "penetration testing",
                 "vulnerability assessment", "security compliance", "firewalls", "siem",
                 "threat intelligence", "risk management", "cryptography", "forensics"],
        "keywords": ["cyber defense", "security operations", "soc", "nist", "iso 27001",
                   "owasp", "zero trust", "endpoint protection"],
        "certifications": ["CISSP", "CEH", "CompTIA Security+"]
    },
    "Full Stack Developer": {
        "skills": ["web development", "mobile development", "backend development", "frontend development",
                 "full-stack development", "full-stack web development", "full-stack mobile development",
                 "full-stack backend development", "full-stack frontend development", "full-stack web development"],
        "keywords": ["html", "css", "javascript", "react", "vue", "angular", "node.js", "express", "django", "flask", "spring boot"],
        "certifications": ["AWS Certified Cloud Practitioner", "AWS Certified Developer", "AWS Certified Solutions Architect"]
    },
    "Cloud Engineer": {
        "skills": ["cloud computing", "amazon web services", "google cloud platform", "azure", "devops", "terraform",   
                 "docker", "kubernetes", "aws lambda", "aws ec2", "aws s3", "aws rds", "aws cloudfront", "aws cloudwatch",
                 "aws cloudtrail", "aws cloudformation", "aws route 53", "aws api gateway", "aws cognito", "aws ssm"],  
        "keywords": ["ec2", "s3", "rds", "lambda", "cloudfront", "cloudwatch", "cloudtrail", "cloudformation", "route 53", "api gateway", "cognito", "ssm"],   
        "certifications": ["AWS Certified Cloud Practitioner", "AWS Certified Developer", "AWS Certified Solutions Architect"]  
        
    "Product Manager"  },
      # [Other roles with similar structure...]
}

# ATS scoring parameters
ATS_PARAMS = {
    "keyword_density": 0.3,
    "section_completeness": 0.25,
    "readability": 0.2,
    "contact_info": 0.15,
    "length_score": 0.1
}

# Load NLP model
try:
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
except:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

def extract_text(file_path):
    """Enhanced text extraction with better PDF handling"""
    text = ""
    try:
        if file_path.lower().endswith(".pdf"):
            with fitz.open(file_path) as doc:
                text = " ".join([page.get_text() for page in doc])
        elif file_path.lower().endswith(".docx"):
            text = docx2txt.process(file_path)
        
        text = re.sub(r'[^\w\s\+\-\/\&]', ' ', text)  
        text = re.sub(r'\s+', ' ', text).strip().lower()
        return text
    except Exception as e:
        print(f"⚠️ Extraction Error: {str(e)[:200]}...")
        return ""

def preprocess_text(text):
    """Advanced cleaning with skill preservation"""
    skill_phrases = set()
    for role in TECH_ROLES.values():
        skill_phrases.update(phrase.replace(" ", "_") for phrase in role["skills"])
    
    for phrase in skill_phrases:
        text = text.replace(phrase.replace("_", " "), phrase)
    
    doc = nlp(text)
    processed = []
    
    for token in doc:
        if not token.is_stop and not token.is_punct and len(token.text) > 2:
            if token.text in skill_phrases:
                processed.append(token.text.replace("_", " "))
            else:
                processed.append(token.lemma_)
    
    return " ".join(processed)

def calculate_ats_score(resume_text):
    """Calculate ATS compatibility score"""
    score = 0
    
    # Check for standard resume sections
    sections = ["experience", "education", "skills", "projects"]
    section_score = sum(1 for section in sections if section in resume_text) / len(sections)
    score += section_score * ATS_PARAMS["section_completeness"]
    
    # Check for contact information
    contact_items = ["email", "phone", "linkedin"]
    contact_score = sum(1 for item in contact_items if item in resume_text) / len(contact_items)
    score += contact_score * ATS_PARAMS["contact_info"]
    
    # Calculate keyword density
    words = resume_text.split()
    unique_words = len(set(words))
    keyword_density = min(1, unique_words / 100)
    score += keyword_density * ATS_PARAMS["keyword_density"]
    
    # Readability score
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    readability = max(0, min(1, (6 - avg_word_length/5)))
    score += readability * ATS_PARAMS["readability"]
    
    # Length score (1-2 pages ideal)
    word_count = len(words)
    length_score = 1 - abs(word_count - 500)/500
    score += max(0, length_score) * ATS_PARAMS["length_score"]
    
    return min(100, round(score * 100))

def calculate_similarity(resume_text, role_data):
    """Combined TF-IDF and exact matching with skill weights"""
    all_skills = role_data["skills"] + role_data["keywords"]
    
    # Exact matching with weights
    skill_counts = Counter()
    total_skills = 0
    
    for skill in all_skills:
        pattern = r'(^|\W)' + re.escape(skill) + r'($|\W)'
        matches = re.findall(pattern, resume_text)
        if matches:
            skill_counts[skill] += len(matches)
        total_skills += 1
    
    exact_match_score = sum(skill_counts.values()) / total_skills
    
    # TF-IDF similarity
    vectorizer = TfidfVectorizer(ngram_range=(1, 3), token_pattern=r'(?u)\b[\w-]+\b')
    try:
        tfidf_matrix = vectorizer.fit_transform([resume_text, ' '.join(all_skills)])
        tfidf_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    except:
        tfidf_score = 0
    
    # Combined score
    final_score = 0.6 * exact_match_score + 0.4 * tfidf_score
    
    # Get top matched skills
    matched_skills = []
    for skill in role_data["skills"]:
        if skill in skill_counts:
            matched_skills.append(skill)
    
    for keyword in role_data["keywords"]:
        if keyword in skill_counts and keyword not in matched_skills:
            matched_skills.append(keyword)
    
    return {
        "score": min(100, round(final_score * 100, 1)),
        "matched_skills": matched_skills,
        "details": {
            "Exact Match": round(exact_match_score * 100, 1),
            "TF-IDF": round(tfidf_score * 100, 1)
        }
    }

def analyze_resume(file_path):
    """Main function to analyze resume"""
    resume_text = extract_text(file_path)
    if not resume_text:
        return {"error": "Could not extract text from file"}
    
    processed_text = preprocess_text(resume_text)
    ats_score = calculate_ats_score(resume_text)
    
    results = {}
    for role, role_data in TECH_ROLES.items():
        results[role] = calculate_similarity(processed_text, role_data)
    
    analysis_results = sorted(results.items(), key=lambda x: x[1]["score"], reverse=True)
    
    return {
        "sample_text": resume_text[:300] + "...",
        "analysis": analysis_results,
        "ats_score": ats_score,
        "filename": file_path.split("/")[-1]
    }

def generate_console_report(analysis_results, ats_score, top_n=3):
    """Generate formatted console output"""
    print("\n" + "="*80)
    print(" " * 30 + "🚀 RESUME ANALYSIS REPORT")
    print("="*80)
    
    print(f"\n📊 ATS Compatibility Score: {ats_score}%")
    print("\n🔝 TOP RECOMMENDED ROLES:")
    for role, data in analysis_results[:top_n]:
        print(f"\n⭐ {role} → {data['score']}% Match")
        print(f"   🛠️ Key Skills: {', '.join(data['matched_skills'][:8])}")
    
    top_role = analysis_results[0][0]
    missing_skills = set(TECH_ROLES[top_role]["skills"]) - set(analysis_results[0][1]["matched_skills"])
    
    if missing_skills:
        print(f"\n🔎 To improve as {top_role}, consider adding these skills:")
        print(" • " + "\n • ".join(sorted(missing_skills)[:5]))
    
    print("\n💡 ACTIONABLE RECOMMENDATIONS:")
    print(f"1. Highlight: {', '.join(analysis_results[0][1]['matched_skills'][:3])}")
    print("2. Add quantifiable achievements")
    print(f"3. Consider: {np.random.choice(TECH_ROLES[top_role]['certifications'])} certification")