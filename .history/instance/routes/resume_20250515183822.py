# resume_parser.py
import re
import os
import PyPDF2
import docx
import spacy
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, List, Tuple
from flask import jsonify

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

TECH_ROLES = {
    "AI/ML Engineer": {
        "keywords": ["machine learning", "deep learning", "python", "tensorflow", "pytorch",
                     "neural networks", "nlp", "computer vision", "data analysis",
                     "scikit-learn", "keras", "artificial intelligence"],
        "description": "Builds intelligent systems using ML/DL models."
    },
    "Data Scientist": {
        "keywords": ["python", "r", "sql", "data analysis", "statistics",
                     "pandas", "numpy", "matplotlib", "seaborn", "tableau",
                     "power bi", "big data"],
        "description": "Extracts insights from complex data."
    },
    "Cloud Engineer": {
        "keywords": ["aws", "azure", "google cloud", "docker", "kubernetes",
                     "terraform", "ci/cd", "devops", "infrastructure", "networking",
                     "serverless", "security"],
        "description": "Designs and manages scalable cloud infrastructure."
    },
    "Cybersecurity Analyst": {
        "keywords": ["cybersecurity", "ethical hacking", "penetration testing",
                     "vulnerability assessment", "firewall", "siem",
                     "incident response", "risk management", "encryption"],
        "description": "Defends systems by identifying and mitigating risks."
    },
    "Full Stack Developer": {
        "keywords": ["javascript", "html", "css", "react", "angular",
                     "node.js", "express", "django", "flask", "api",
                     "mongodb", "mysql", "responsive design"],
        "description": "Develops both frontend and backend web applications."
    },
    "DevOps Engineer": {
        "keywords": ["devops", "jenkins", "ansible", "docker", "kubernetes",
                     "ci/cd", "aws", "azure", "automation", "monitoring"],
        "description": "Streamlines software delivery with CI/CD pipelines."
    },
    "Blockchain Developer": {
        "keywords": ["blockchain", "solidity", "ethereum", "smart contracts",
                     "cryptography", "web3", "dapps", "hyperledger"],
        "description": "Creates decentralized applications on blockchain platforms."
    },
    "UI/UX Designer": {
        "keywords": ["ui", "ux", "figma", "adobe xd", "sketch", "wireframing",
                     "prototyping", "user research", "usability testing"],
        "description": "Designs intuitive and engaging user interfaces."
    },
    "Product Manager": {
        "keywords": ["product management", "agile", "scrum", "roadmapping",
                     "stakeholder management", "user stories", "prioritization"],
        "description": "Leads product lifecycle from concept to launch."
    },
    "Software Engineer": {
        "keywords": ["java", "python", "c++", "algorithms", "data structures",
                     "oop", "design patterns", "debugging", "testing"],
        "description": "Develops and maintains scalable software solutions."
    }
}

ATS_KEYWORDS = [
    "achieved", "improved", "optimized", "developed", "implemented",
    "led", "managed", "increased", "reduced", "engineered", "collaborated",
    "designed", "built", "created", "launched", "delivered", "solved",
    "transformed", "enhanced", "automated", "scaled"
]

IMPROVEMENT_SUGGESTIONS = {
    "quantifiable": {
        "text": "Include quantifiable achievements (e.g., 'Improved performance by 30%').",
        "priority": "high"
    },
    "action_verbs": {
        "text": "Start bullet points with strong action verbs.",
        "priority": "high"
    },
    "length_short": {
        "text": "Resume seems too short. Add more details about your achievements.",
        "priority": "medium"
    },
    "length_long": {
        "text": "Resume seems too long. Keep it concise (1-2 pages).",
        "priority": "medium"
    },
    "keywords": {
        "text": "Add more role-specific keywords to match job descriptions.",
        "priority": "high"
    },
    "formatting": {
        "text": "Use consistent formatting and readable fonts.",
        "priority": "medium"
    },
    "customization": {
        "text": "Tailor resume for each job application.",
        "priority": "low"
    },
    "contact_info": {
        "text": "Ensure contact information is clearly visible.",
        "priority": "high"
    },
    "education": {
        "text": "Include education details if missing.",
        "priority": "medium"
    },
    "experience_gaps": {
        "text": "Explain any significant employment gaps.",
        "priority": "medium"
    }
}

class ResumeAnalyzer:
    def __init__(self):
        self.roles = TECH_ROLES
        self.ats_keywords = ATS_KEYWORDS
        self.improvement_suggestions = IMPROVEMENT_SUGGESTIONS

    def extract_text(self, file_path: str) -> str:
        """Extract text from PDF or DOCX file."""
        text = ""
        try:
            if file_path.lower().endswith(".pdf"):
                with open(file_path, "rb") as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        text += page.extract_text() or ""
            elif file_path.lower().endswith(".docx"):
                doc = docx.Document(file_path)
                text = "\n".join(para.text for para in doc.paragraphs)
            else:
                raise ValueError("Unsupported file format. Please upload PDF or DOCX.")
        except Exception as e:
            raise Exception(f"Error extracting text: {str(e)}")
        return text.lower()

    def preprocess_text(self, text: str) -> str:
        """Clean and normalize text for analysis."""
        text = re.sub(r"[^a-z0-9\s]", " ", text)  # Remove special chars
        text = re.sub(r"\s+", " ", text).strip()  # Normalize whitespace
        return text

    def calculate_ats_score(self, text: str) -> Tuple[float, str]:
        """Calculate ATS compatibility score with feedback."""
        counts = Counter(text.split())
        hits = sum(counts.get(k, 0) for k in self.ats_keywords)
        max_hits = len(self.ats_keywords) * 3  # Reasonable max occurrences
        
        # Calculate base score
        score = min(100.0, (hits / max_hits) * 100) if max_hits else 0.0
        score = round(score, 1)
        
        # Generate feedback
        if score >= 85:
            feedback = "Excellent! Your resume is well-optimized for ATS systems."
        elif score >= 70:
            feedback = "Good. Your resume performs well but could use some improvements."
        elif score >= 50:
            feedback = "Fair. Your resume may have trouble passing through ATS filters."
        else:
            feedback = "Needs significant work. Your resume is not well-optimized for ATS."
            
        return score, feedback

    def recommend_roles(self, text: str) -> Dict:
        """Recommend best matching roles based on resume content."""
        cleaned = self.preprocess_text(text)
        
        # Prepare documents for similarity comparison
        docs = [cleaned]
        role_names = []
        role_descriptions = []
        
        for name, info in self.roles.items():
            role_names.append(name)
            role_descriptions.append(" ".join(info["keywords"]) + " " + info["description"])
            docs.append(role_descriptions[-1])
        
        # Calculate TF-IDF and cosine similarity
        try:
            tfidf = TfidfVectorizer().fit_transform(docs)
            similarities = cosine_similarity(tfidf[0:1], tfidf[1:])[0]
            
            # Rank roles by similarity score
            ranked_roles = sorted(zip(role_names, similarities), 
                               key=lambda x: x[1], reverse=True)
            
            best_match, best_score = ranked_roles[0]
            
            return {
                "best_match": best_match,
                "match_score": round(best_score * 100, 1),
                "top_matches": [{"role": r, "score": round(s * 100, 1)} 
                               for r, s in ranked_roles[:5]],
                "role_details": {
                    "description": self.roles[best_match]["description"],
                    "keywords": self.roles[best_match]["keywords"][:10]
                }
            }
        except Exception as e:
            print(f"Error in role recommendation: {str(e)}")
            # Fallback to default if analysis fails
            return {
                "best_match": "Software Engineer",
                "match_score": 75.0,
                "top_matches": [
                    {"role": "Software Engineer", "score": 75.0},
                    {"role": "Full Stack Developer", "score": 65.0},
                    {"role": "DevOps Engineer", "score": 60.0}
                ],
                "role_details": {
                    "description": self.roles["Software Engineer"]["description"],
                    "keywords": self.roles["Software Engineer"]["keywords"][:10]
                }
            }

    def extract_skills(self, text: str) -> List[str]:
        """Extract relevant skills from resume text."""
        all_skills = {kw for info in self.roles.values() for kw in info["keywords"]}
        found_skills = [s for s in all_skills if s in text]
        
        # Also look for skills in noun phrases
        doc = nlp(text)
        noun_phrases = {chunk.text.lower() for chunk in doc.noun_chunks}
        found_skills.extend([s for s in all_skills if s in noun_phrases])
        
        return sorted(list(set(found_skills)), key=lambda x: -len(x))[:15]  # Return top 15 unique skills

    def extract_experience(self, text: str) -> Dict:
        """Extract experience and education details."""
        # Extract years of experience
        years = 0
        experience_patterns = [
            r"(\d+)\+?\s*years?\s*experience",
            r"experience:\s*(\d+)",
            r"(\d+)\s*years?\s*in\s*[a-z\s]+"
        ]
        
        for pattern in experience_patterns:
            match = re.search(pattern, text)
            if match:
                years = max(years, int(match.group(1)))
                break
        
        # Extract education
        education = []
        edu_patterns = [
            r"(bachelor['s]?\s*of\s*\w+)\s*[,-]?\s*([a-z\s]+university[^\n]*)",
            r"(master['s]?\s*of\s*\w+)\s*[,-]?\s*([a-z\s]+university[^\n]*)",
            r"(ph\.?d)\s*[,-]?\s*([a-z\s]+university[^\n]*)",
            r"education\s*:\s*([^\n]+)"
        ]
        
        for pattern in edu_patterns:
            matches = re.finditer(pattern, text)
            for match in matches:
                degree = match.group(1).title()
                if match.lastindex > 1:
                    institution = match.group(2).title()
                    education.append(f"{degree} - {institution}")
                else:
                    education.append(degree)
        
        return {
            "years": years,
            "education": list(set(education))[:3]  # Return unique entries, max 3
        }

    def suggest_improvements(self, text: str) -> List[Dict]:
        """Generate improvement suggestions based on resume analysis."""
        suggestions = []
        
        # Check for quantifiable achievements
        if not re.search(r"\d+%|\$\d+|\d+\+", text):
            suggestions.append(self.improvement_suggestions["quantifiable"])
        
        # Check for action verbs
        action_verb_count = sum(text.count(verb) for verb in self.ats_keywords)
        if action_verb_count < 5:
            suggestions.append(self.improvement_suggestions["action_verbs"])
        
        # Check resume length
        word_count = len(text.split())
        if word_count < 200:
            suggestions.append(self.improvement_suggestions["length_short"])
        elif word_count > 800:
            suggestions.append(self.improvement_suggestions["length_long"])
        
        # Check for contact info
        if not re.search(r"phone|email|contact", text):
            suggestions.append(self.improvement_suggestions["contact_info"])
        
        # Check for education section
        if not any(edu in text for edu in ["university", "college", "degree", "bachelor", "master"]):
            suggestions.append(self.improvement_suggestions["education"])
        
        # Always include these suggestions
        suggestions.extend([
            self.improvement_suggestions["keywords"],
            self.improvement_suggestions["formatting"],
            self.improvement_suggestions["customization"]
        ])
        
        return suggestions[:5]  # Return top 5 most important suggestions

    def analyze_resume(self, file_path: str) -> Dict:
        """Main method to analyze a resume file."""
        try:
            # Step 1: Extract text from file
            raw_text = self.extract_text(file_path)
            
            # Step 2: Calculate ATS score
            ats_score, ats_feedback = self.calculate_ats_score(raw_text)
            
            # Step 3: Recommend roles
            role_recommendations = self.recommend_roles(raw_text)
            
            # Step 4: Extract skills
            skills = self.extract_skills(raw_text)
            
            # Step 5: Extract experience
            experience = self.extract_experience(raw_text)
            
            # Step 6: Generate improvement suggestions
            improvements = self.suggest_improvements(raw_text)
            
            return {
                "success": True,
                "ats_score": ats_score,
                "ats_feedback": ats_feedback,
                "role_match": role_recommendations,
                "skills": skills,
                "experience": experience,
                "improvements": improvements,
                "raw_text": raw_text[:1000] + "..." if len(raw_text) > 1000 else raw_text  # For debugging
            }
        except Exception as e:
            print(f"Error analyzing resume: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }