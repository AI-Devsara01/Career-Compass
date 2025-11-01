import re
import spacy
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import docx
from typing import Dict, List, Tuple, Optional

# Load English language model for NLP
nlp = spacy.load("en_core_web_sm")

def extract_text(file_path: str) -> str:
    """Extract text from PDF or DOCX files"""
    text = ""
    try:
        if file_path.endswith('.pdf'):
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text() or ""
        elif file_path.endswith('.docx'):
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                text += para.text + "\n"
        else:
            raise ValueError("Unsupported file format. Please upload PDF or DOCX.")
    except Exception as e:
        raise ValueError(f"Error reading file: {str(e)}")
    
    return text.lower()

def recommend_role(resume_text: str) -> Dict:
    """Recommend the best matching role for the resume"""
    analyzer = ResumeAnalyzer()
    return analyzer.find_best_role_match(resume_text)

class ResumeAnalyzer:
    def __init__(self):
        # Define the 10 tech roles and their required skills
        self.tech_roles = {
            "AI/ML Engineer": {
                "keywords": ["machine learning", "deep learning", "python", "tensorflow", "pytorch", 
                            "neural networks", "natural language processing", "computer vision", 
                            "data analysis", "scikit-learn", "keras", "ai", "artificial intelligence"],
                "description": "Builds intelligent systems using machine learning and deep learning models."
            },
            # ... [rest of your role definitions remain the same]
        }
        
        # Common ATS keywords that boost resume score
        self.ats_keywords = [
            "achieved", "improved", "optimized", "developed", "implemented", 
            "led", "managed", "increased", "reduced", "saved", 
            "collaborated", "designed", "engineered", "automated", "analyzed",
            "quantifiable", "results", "metrics", "kpis", "impact"
        ]
        
        # Resume improvement suggestions
        self.improvement_suggestions = {
            "keywords": "Add more role-specific keywords to better match job descriptions",
            "quantifiable": "Include quantifiable achievements (e.g., 'Improved performance by 30%')",
            "action_verbs": "Start bullet points with strong action verbs",
            "length": "Keep resume concise (1-2 pages for most professionals)",
            "contact": "Ensure contact information is up-to-date and professional",
            "education": "Include relevant education and certifications",
            "skills": "List technical skills prominently with proficiency levels",
            "projects": "Add relevant projects with descriptions and outcomes",
            "formatting": "Use consistent formatting and readable fonts",
            "customization": "Tailor resume for each specific job application"
        }

    def preprocess_text(self, text: str) -> str:
        """Clean and preprocess text for analysis"""
        text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def analyze_resume(self, resume_text: str) -> Dict:
        """Analyze resume and return comprehensive results"""
        cleaned_text = self.preprocess_text(resume_text)
        ats_score = self.calculate_ats_score(cleaned_text)
        role_match = self.find_best_role_match(cleaned_text)
        improvements = self.get_improvement_suggestions(cleaned_text)
        skills = self.extract_skills(cleaned_text)
        experience = self.extract_experience(cleaned_text)
        
        return {
            "ats_score": ats_score,
            "role_match": role_match,
            "improvements": improvements,
            "skills": skills,
            "experience": experience,
            "original_text": resume_text
        }
