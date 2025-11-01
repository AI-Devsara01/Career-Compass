# Import libraries
import numpy as np
import fitz  # PyMuPDF
import docx2txt
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import nltk
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
                   "random forest", "xgboost", "pipeline", "feature engineering"]
    },
    "Data Scientist": {
        "skills": ["data analysis", "data visualization", "statistical modeling", "python", "r", 
                 "sql", "pandas", "numpy", "matplotlib", "seaborn", "scipy", "hypothesis testing",
                 "regression", "classification", "clustering", "time series", "experiment design"],
        "keywords": ["eda", "feature selection", "a/b testing", "power bi", "tableau",
                   "pyspark", "hadoop", "big data", "data mining", "predictive modeling"]
    },
    # [Other roles remain the same...]
}

# Load NLP model
try:
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
except:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

# ========== IMPROVED TEXT PROCESSING ==========
def extract_text(file_path):
    """Enhanced text extraction with better PDF handling"""
    text = ""
    try:
        if file_path.lower().endswith(".pdf"):
            with fitz.open(file_path) as doc:
                text = " ".join([page.get_text() for page in doc])
        elif file_path.lower().endswith(".docx"):
            text = docx2txt.process(file_path)
        
        # Better cleaning preserving important symbols
        text = re.sub(r'[^\w\s\+\-\/\&]', ' ', text)  
        text = re.sub(r'\s+', ' ', text).strip().lower()
        return text
    except Exception as e:
        print(f"⚠️ Extraction Error: {str(e)[:200]}...")
        return ""

def preprocess_text(text):
    """Advanced cleaning with skill preservation"""
    # Keep skill phrases intact
    skill_phrases = set()
    for role in TECH_ROLES.values():
        skill_phrases.update(phrase.replace(" ", "_") for phrase in role["skills"])
    
    # Temporary replacement
    for phrase in skill_phrases:
        text = text.replace(phrase.replace("_", " "), phrase)
    
    doc = nlp(text)
    processed = []
    
    for token in doc:
        if not token.is_stop and not token.is_punct and len(token.text) > 2:
            # Restore original skill phrases
            if token.text in skill_phrases:
                processed.append(token.text.replace("_", " "))
            else:
                processed.append(token.lemma_)
    
    return " ".join(processed)

# ========== ADVANCED ANALYSIS METHODS ==========
def calculate_similarity(resume_text, role_data):
    """Combined TF-IDF and exact matching with skill weights"""
    all_skills = role_data["skills"] + role_data["keywords"]
    
    # Exact matching with weights
    skill_counts = Counter()
    total_skills = 0
    
    for skill in all_skills:
        # Check both standalone and in context
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
    
    # Combined score (60% exact match, 40% TF-IDF)
    final_score = 0.6 * exact_match_score + 0.4 * tfidf_score
    
    # Get top matched skills (unique and ordered by importance)
    matched_skills = []
    for skill in role_data["skills"]:
        if skill in skill_counts:
            matched_skills.append(skill)
    
    for keyword in role_data["keywords"]:
        if keyword in skill_counts and keyword not in matched_skills:
            matched_skills.append(keyword)
    
    return {
        "score": min(100, round(final_score * 100, 1)),  # Cap at 100%
        "matched_skills": matched_skills,
        "details": {
            "Exact Match": round(exact_match_score * 100, 1),
            "TF-IDF": round(tfidf_score * 100, 1)
        }
    }

# ========== GENERATE ENHANCED REPORT ==========
def generate_report(analysis_results, top_n=3):
    print("\n" + "="*80)
    print(" " * 30 + "🚀 ADVANCED RESUME ANALYSIS REPORT")
    print("="*80)
    
    # Top Recommended Roles
    print(f"\n🔝 TOP {top_n} RECOMMENDED ROLES:")
    for role, data in analysis_results[:top_n]:
        print(f"\n⭐ {role} → {data['score']}% Match")
        print(f"   🛠️ Key Skills: {', '.join(data['matched_skills'][:8])}")
        print(f"   📊 Analysis: Exact Match({data['details']['Exact Match']}%) + TF-IDF({data['details']['TF-IDF']}%)")
    
    # Skill Gap Analysis
    print("\n🔎 SKILL GAP ANALYSIS:")
    top_role = analysis_results[0][0]
    missing_skills = set(TECH_ROLES[top_role]["skills"]) - set(analysis_results[0][1]["matched_skills"])
    
    if missing_skills:
        print(f"\nTo improve as {top_role}, consider adding:")
        print(" • " + "\n • ".join(sorted(missing_skills)[:10]))  # Show top 10 missing
    
    # Full Breakdown
    print("\n📊 FULL ROLE COMPATIBILITY:")
    for role, data in analysis_results:
        print(f"\n{role}:")
        progress = min(20, int(data['score'] / 5))  # Cap at 100%
        print(f"   [{'█' * progress}{' ' * (20 - progress)}] {data['score']}%")
        if data['matched_skills']:
            print(f"   ✔️ Strong matches: {', '.join(data['matched_skills'][:5])}")
    
    # Actionable suggestions
    print("\n💡 ACTIONABLE RECOMMENDATIONS:")
    print("1. Highlight these skills in your resume summary:")
    print(f"   • {', '.join(analysis_results[0][1]['matched_skills'][:3])}")
    print("\n2. Add quantifiable achievements like:")
    print("   • 'Improved model accuracy by X% using Y technique'")
    print("   • 'Reduced processing time by X through Y optimization'")
    print("\n3. Consider certifications for:")
    print(f"   • {analysis_results[0][0]} (e.g., {np.random.choice(['AWS ML', 'TensorFlow', 'Google Cloud'])} Certification)")

# ========== EXECUTION ==========
print("📤 Upload your resume (PDF or DOCX):")
uploaded = files.upload()
file_path = next(iter(uploaded))

print("\n🔍 Analyzing your resume...")
resume_text = extract_text(file_path)

# Debug: Show extracted text snippet
print("\n📝 Extracted Text Sample (300 chars):")
print(resume_text[:300] + "...\n")

# Enhanced analysis
results = {}
for role, role_data in TECH_ROLES.items():
    results[role] = calculate_similarity(resume_text, role_data)

# Sort by score
analysis_results = sorted(results.items(), key=lambda x: x[1]["score"], reverse=True)

# Generate comprehensive report
generate_report(analysis_results)