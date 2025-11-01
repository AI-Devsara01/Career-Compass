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
def get_improvement_suggestions(self, text: str) -> List[Dict]:
        """Generate personalized improvement suggestions"""
        suggestions = []
        
        # Check for quantifiable achievements
        quantifiable_patterns = [
            r'\d+%', r'\$\d+', r'\d+\+', r'increased by', r'reduced by', 
            r'saved \$\d+', r'improved by', r'by \d+'
        ]
        has_quantifiable = any(re.search(pattern, text) for pattern in quantifiable_patterns)
        
        if not has_quantifiable:
            suggestions.append({
                "category": "quantifiable",
                "suggestion": self.improvement_suggestions["quantifiable"],
                "priority": "high"
            })
        
        # Check for action verbs
        action_verbs = ["achieved", "improved", "developed", "led", "managed", 
                       "increased", "reduced", "optimized", "implemented"]
        has_action_verbs = any(verb in text for verb in action_verbs)
        
        if not has_action_verbs:
            suggestions.append({
                "category": "action_verbs",
                "suggestion": self.improvement_suggestions["action_verbs"],
                "priority": "medium"
            })
        
        # Check resume length (approximate)
        word_count = len(text.split())
        if word_count < 200:
            suggestions.append({
                "category": "length",
                "suggestion": "Resume seems too short. Consider adding more details about your experience and skills.",
                "priority": "high"
            })
        elif word_count > 600:
            suggestions.append({
                "category": "length",
                "suggestion": "Resume seems too long. Consider making it more concise (1-2 pages).",
                "priority": "medium"
            })
        
        # Add standard suggestions
        standard_suggestions = ["keywords", "skills", "projects", "formatting", "customization"]
        for suggestion in standard_suggestions:
            suggestions.append({
                "category": suggestion,
                "suggestion": self.improvement_suggestions[suggestion],
                "priority": "low"
            })
        
        return suggestions

    def extract_skills(self, text: str) -> List[str]:
        """Extract skills from resume text"""
        # Get all skills from all roles
        all_skills = set()
        for role_data in self.tech_roles.values():
            for skill in role_data["keywords"]:
                all_skills.add(skill.lower())
        
        # Find skills mentioned in resume
        found_skills = [skill for skill in all_skills if skill in text]
        
        return sorted(found_skills, key=lambda x: -len(x))

    def extract_experience(self, text: str) -> Dict:
        """Extract basic experience information (simplified)"""
        # Look for experience patterns
        experience = {
            "years": 0,
            "jobs": [],
            "education": []
        }
        
        # Try to find years of experience
        year_patterns = [
            r'(\d+)\+? years? of experience',
            r'experience:?\s*(\d+)\+? years?',
            r'(\d+)\+? yrs?'
        ]
        
        for pattern in year_patterns:
            match = re.search(pattern, text)
            if match:
                experience["years"] = int(match.group(1))
                break
        
        # Extract education (simplified)
        education_keywords = ["university", "college", "institute", "bachelor", "master", "phd", "degree"]
        education_lines = [line for line in text.split('\n') 
                          if any(keyword in line for keyword in education_keywords)]
        experience["education"] = education_lines[:3]  # Return up to 3 education entries
        
        return experience

    def analyze_resume_file(self, file_path: str) -> Dict:
        """Analyze resume from file path"""
        try:
            # Extract text from file using the standalone function
            resume_text = extract_text_from_file(file_path)
            
            # Analyze the resume
            analysis_results = self.analyze_resume(resume_text)
            
            return analysis_results

        except Exception as e:
            return {"error": str(e)}