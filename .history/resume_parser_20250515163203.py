# resume_parser.py
import re
import os
import PyPDF2
import docx
import spacy
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, List

# Load SpaCy English model (make sure to pip install spacy and python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

# Tech roles with keywords & descriptions
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
        "description": "Designs and manages scalable cloud infra."
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

# Common ATS action verbs
ATS_KEYWORDS = [
    "achieved", "improved", "optimized", "developed", "implemented",
    "led", "managed", "increased", "reduced", "engineered", "collaborated"
]

IMPROVEMENT_SUGGESTIONS = {
    "quantifiable": "Include quantifiable achievements (e.g., 'Improved performance by 30%').",
    "action_verbs": "Start bullet points with strong action verbs.",
    "length_short": "Resume seems too short. Add more details about your achievements.",
    "length_long": "Resume seems too long. Keep it concise (1–2 pages).",
    "keywords": "Add more role-specific keywords to match job descriptions.",
    "formatting": "Use consistent formatting and readable fonts.",
    "customization": "Tailor resume for each job application."
}

class ResumeAnalyzer:
    def _init_(self):
        self.roles = TECH_ROLES
        self.ats_keywords = ATS_KEYWORDS

    def extract_text(self, file_path: str) -> str:
        """Extract text from PDF or DOCX."""
        text = ""
        if file_path.lower().endswith(".pdf"):
            with open(file_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text() or ""
        elif file_path.lower().endswith(".docx"):
            doc = docx.Document(file_path)
            text = "\n".join(para.text for para in doc.paragraphs)
        else:
            raise ValueError("Unsupported format: upload PDF or DOCX")
        return text.lower()

    def preprocess(self, text: str) -> str:
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        return re.sub(r"\s+", " ", text).strip()

    def calculate_ats_score(self, text: str) -> float:
        counts = Counter(text.split())
        hits = sum(counts.get(k, 0) for k in self.ats_keywords)
        max_hits = len(self.ats_keywords) * 3
        score = min(100.0, (hits / max_hits) * 100) if max_hits else 0.0
        return round(score, 1)

    def recommend_roles(self, text: str) -> Dict:
        """Return best role match and top 3 matches by cosine similarity."""
        cleaned = self.preprocess(text)
        docs = [cleaned]
        names, descs = [], []
        for name, info in self.roles.items():
            names.append(name)
            descs.append(" ".join(info["keywords"]) + " " + info["description"])
            docs.append(descs[-1])

        tfidf = TfidfVectorizer().fit_transform(docs)
        sim = cosine_similarity(tfidf[0:1], tfidf[1:])[0]
        ranked = sorted(zip(names, sim), key=lambda x: x[1], reverse=True)
        best, best_score = ranked[0]
        return {
            "best_match": best,
            "match_score": round(best_score * 100, 1),
            "top_matches": [{"role": r, "score": round(s * 100, 1)} for r, s in ranked[:3]],
            "description": self.roles[best]["description"]
        }

    def extract_skills(self, text: str) -> List[str]:
        all_skills = {kw for info in self.roles.values() for kw in info["keywords"]}
        return [s for s in all_skills if s in text]

    def extract_experience(self, text: str) -> Dict:
        yrs = 0
        for pat in [r"(\d+)\+?\s*years?", r"experience:\s*(\d+)"]:
            m = re.search(pat, text)
            if m:
                yrs = int(m.group(1))
                break
        edu = [line for line in text.splitlines()
               if any(k in line for k in ["university", "college", "bachelor", "master", "phd"])]
        return {"years": yrs, "education": edu[:3]}

    def suggest_improvements(self, text: str) -> List[Dict]:
        sug = []
        if not re.search(r"\d+%", text):
            sug.append({"category": "quantifiable", "suggestion": IMPROVEMENT_SUGGESTIONS["quantifiable"]})
        if not any(v in text for v in self.ats_keywords):
            sug.append({"category": "action_verbs", "suggestion": IMPROVEMENT_SUGGESTIONS["action_verbs"]})
        wc = len(text.split())
        if wc < 200:
            sug.append({"category": "length", "suggestion": IMPROVEMENT_SUGGESTIONS["length_short"]})
        elif wc > 600:
            sug.append({"category": "length", "suggestion": IMPROVEMENT_SUGGESTIONS["length_long"]})
        for cat in ["keywords", "formatting", "customization"]:
            sug.append({"category": cat, "suggestion": IMPROVEMENT_SUGGESTIONS[cat]})
        return sug

    def analyze_file(self, path: str) -> Dict:
        text = self.extract_text(path)
        ats = self.calculate_ats_score(text)
        roles = self.recommend_roles(text)
        skills = self.extract_skills(text)
        exp = self.extract_experience(text)
        imps = self.suggest_improvements(text)
        return {
            "ats_score": ats,
            "role_match": roles,
            "skills": skills,
            "experience": exp,
            "suggestions": imps
        }