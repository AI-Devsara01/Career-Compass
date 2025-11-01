import re
import os
import PyPDF2
import docx
import spacy
import nltk
from nltk.corpus import stopwords
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, List, Tuple
import pdfplumber
from datetime import datetime

# Initialize NLP
nlp = spacy.load("en_core_web_sm")
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

class ResumeParser:
    def __init__(self):
        self.tech_roles = self._load_tech_roles()
        self.ats_keywords = self._load_ats_keywords()
        self.improvement_suggestions = self._load_improvement_suggestions()
        self.skill_db = self._load_skill_database()
        
    def _load_tech_roles(self) -> Dict:
        return {
            "AI/ML Engineer": {
                "keywords": ["machine learning", "deep learning", "python", "tensorflow", "pytorch",
                            "neural networks", "nlp", "computer vision", "data analysis",
                            "scikit-learn", "keras", "artificial intelligence", "llm", "transformers"],
                "description": "Builds intelligent systems using ML/DL models."
            },
            # [Other roles remain the same as in your original code]
        }
    
    def _load_ats_keywords(self) -> List[str]:
        return [
            "achieved", "improved", "optimized", "developed", "implemented",
            "led", "managed", "increased", "reduced", "engineered", "collaborated",
            "designed", "built", "transformed", "delivered", "spearheaded", 
            "mentored", "automated", "scaled", "innovated", "quantified"
        ]
    
    def _load_improvement_suggestions(self) -> Dict:
        return {
            "quantifiable": {
                "title": "Add Metrics",
                "description": "Include quantifiable achievements (e.g., 'Improved performance by 30%')",
                "priority": "high"
            },
            # [Other suggestions...]
        }
    
    def _load_skill_database(self) -> List[str]:
        return [
            "python", "java", "aws", "azure", "docker", "kubernetes",
            # [200+ other skills...]
        ]
    
    def extract_text(self, file_path: str) -> str:
        """Extract text from PDF or DOCX with improved parsing"""
        text = ""
        
        try:
            if file_path.lower().endswith('.pdf'):
                with pdfplumber.open(file_path) as pdf:
                    for page in pdf.pages:
                        text += page.extract_text() or ""
            elif file_path.lower().endswith('.docx'):
                doc = docx.Document(file_path)
                text = "\n".join(para.text for para in doc.paragraphs)
            else:
                raise ValueError("Unsupported file format")
        except Exception as e:
            raise Exception(f"Error extracting text: {str(e)}")
        
        return text.lower()
    
    def preprocess_text(self, text: str) -> str:
        """Advanced text cleaning and normalization"""
        # Remove special chars but keep % for metrics
        text = re.sub(r"[^a-zA-Z0-9\s%+]", " ", text)
        # Normalize whitespace
        text = re.sub(r"\s+", " ", text).strip()
        # Remove stopwords
        words = text.split()
        filtered_words = [word for word in words if word not in stop_words]
        return " ".join(filtered_words)
    
    def calculate_ats_score(self, text: str) -> Tuple[float, Dict]:
        """Comprehensive ATS scoring with multiple factors"""
        score_components = {}
        
        # Keyword matching
        keyword_counts = Counter(text.split())
        hits = sum(keyword_counts.get(k, 0) for k in self.ats_keywords)
        max_hits = len(self.ats_keywords) * 3  # Assume max 3 mentions per keyword is ideal
        keyword_score = min(100, (hits / max_hits) * 100) if max_hits else 0
        score_components["keywords"] = keyword_score
        
        # Quantifiable achievements
        quantifiable = len(re.findall(r"\d+%|\$\d+|\d+\+", text))
        quant_score = min(100, quantifiable * 10)  # 10 points per quantifiable metric
        score_components["quantifiable"] = quant_score
        
        # Length analysis (ideal 400-600 words)
        word_count = len(text.split())
        if word_count < 300:
            length_score = 30
        elif word_count > 800:
            length_score = 70
        else:
            length_score = 100
        score_components["length"] = length_score
        
        # Section completeness (education, experience, skills)
        sections = 0
        for sec in ["education", "experience", "skills", "projects"]:
            if sec in text:
                sections += 1
        section_score = (sections / 4) * 100
        score_components["sections"] = section_score
        
        # Final weighted score
        weights = {
            "keywords": 0.4,
            "quantifiable": 0.3,
            "length": 0.2,
            "sections": 0.1
        }
        final_score = sum(score_components[comp] * weights[comp] for comp in score_components)
        
        return round(final_score, 1), score_components
    
    def extract_experience(self, text: str) -> Dict:
        """Enhanced experience extraction with duration parsing"""
        experience = {
            "total_years": 0,
            "positions": [],
            "education": []
        }
        
        # Extract duration patterns
        duration_patterns = [
            r"(\d+)\s*(?:years?|yrs?)",
            r"experience.*?(\d+)",
            r"(\d+)\+?\s*years?\s*experience"
        ]
        
        for pattern in duration_patterns:
            match = re.search(pattern, text)
            if match:
                experience["total_years"] = int(match.group(1))
                break
        
        # Extract position timelines
        position_pattern = r"(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s*\d{4}\s*(?:to|-|present)\s*(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s*\d{4}"
        experience["positions"] = re.findall(position_pattern, text)
        
        # Extract education
        edu_patterns = [
            r"(university|college|institute|school).*?(bachelor|master|phd|bs|ms|ph\.?d)",
            r"(b\.?sc|m\.?sc|b\.?tech|m\.?tech).*?(computer|engineering|science)"
        ]
        
        for line in text.split('\n'):
            for pattern in edu_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    experience["education"].append(line.strip())
                    break
        
        return experience
    
    def analyze_resume(self, file_path: str) -> Dict:
        """Complete resume analysis pipeline"""
        try:
            raw_text = self.extract_text(file_path)
            clean_text = self.preprocess_text(raw_text)
            
            # Core analysis
            ats_score, score_components = self.calculate_ats_score(clean_text)
            experience = self.extract_experience(raw_text)  # Use raw text for better pattern matching
            
            # Generate suggestions
            suggestions = self.generate_suggestions(raw_text, clean_text, ats_score)
            
            return {
                "success": True,
                "ats_score": ats_score,
                "score_components": score_components,
                "experience": experience,
                "suggestions": suggestions,
                "word_count": len(raw_text.split()),
                "text_samples": {
                    "summary": self.extract_summary(raw_text),
                    "achievements": self.extract_achievements(raw_text)
                }
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    # [Additional helper methods...]