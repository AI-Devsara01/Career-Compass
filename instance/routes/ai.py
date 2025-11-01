from flask import Blueprint, render_template, session, redirect, url_for

ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/ai_engineer/internships')
def ai_internships():
    internships = [
        {
            "company": "TCS",
            "role": "AI Research Intern",
            "title": "AI Research Intern at TCS Research",
            "description": "Build NLP and Computer Vision solutions for enterprise applications.",
            "requirements": "Proficiency in Python, Transformers, and knowledge of research methods.",
            "location": "Mumbai, Maharashtra",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://www.tcs.com/careers"
        },
        {
            "company": "Wipro",
            "role": "AI Intern",
            "title": "AI Intern at Wipro",
            "description": "Contribute to automation and data intelligence platforms using AI models.",
            "requirements": "Strong foundations in machine learning, Pandas, and deployment basics.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://careers.wipro.com"
        },
        {
            "company": "Zoho Corp",
            "role": "ML Intern",
            "title": "Machine Learning Intern at Zoho",
            "description": "Develop intelligent modules for CRM automation and email filtering.",
            "requirements": "Data wrangling skills, Scikit-learn, and understanding of unsupervised learning.",
            "location": "Chennai, Tamil Nadu",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://www.zoho.com/careers"
        },
        {
            "company": "CRED",
            "role": "AI Product Intern",
            "title": "AI Intern at CRED",
            "description": "Apply AI for fraud detection and personalized credit scoring.",
            "requirements": "Experience with model deployment, real-time data streaming (Kafka).",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://cred.club"
        },
        {
            "company": "Fractal Analytics",
            "role": "AI Analyst Intern",
            "title": "AI Analyst Intern at Fractal Analytics",
            "description": "Assist with analytical projects involving ML and statistical modeling.",
            "requirements": "Python, NumPy, basic stats, and EDA with Pandas/Seaborn.",
            "location": "Mumbai, Maharashtra",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://fractal.ai"
        },
        {
            "company": "Amazon India",
            "role": "Applied Scientist Intern",
            "title": "Applied Scientist Intern at Amazon India",
            "description": "Work on recommendation systems and inventory forecasting using ML.",
            "requirements": "Knowledge of supervised learning, AWS ML stack, and SQL.",
            "location": "Hyderabad, Telangana",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.amazon.jobs"
        },
        {
            "company": "Google India",
            "role": "AI/ML Intern",
            "title": "AI/ML Intern at Google India",
            "description": "Participate in cutting-edge research in NLP and computer vision.",
            "requirements": "Python, TensorFlow, PyTorch, and deep learning fundamentals.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://careers.google.com"
        },
        {
            "company": "Intel India",
            "role": "AI Intern",
            "title": "AI Intern at Intel India",
            "description": "Develop ML-based solutions for embedded and edge devices.",
            "requirements": "Machine learning, OpenVINO, and hardware-aware ML design.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://jobs.intel.com"
        },
        {
            "company": "Adobe India",
            "role": "AI Research Intern",
            "title": "AI Research Intern at Adobe India",
            "description": "Innovate in intelligent design tools powered by deep learning.",
            "requirements": "Image processing, CNNs, PyTorch, and good writing skills for research.",
            "location": "Noida, Uttar Pradesh",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced"
        },
        {
            "company": "Flipkart",
            "role": "ML Intern",
            "title": "Machine Learning Intern at Flipkart",
            "description": "Optimize delivery routes and warehouse analytics using ML models.",
            "requirements": "Data preprocessing, sklearn, and logistic regression.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://www.flipkartcareers.com"
        },
        {
    "company": "NVIDIA",
    "role": "Deep Learning Intern",
    "title": "Deep Learning Intern at NVIDIA India",
    "description": "Support the development of AI models for GPU-accelerated applications.",
    "requirements": "CUDA, PyTorch, parallel computing, and DL optimization.",
    "location": "Pune, Maharashtra",
    "start_date": "June 2025",
    "end_date": "August 2025",
    "duration": "3 months",
    "apply_link": "https://www.nvidia.com/en-in/about-nvidia/careers/"
},
{
    "company": "Jio Platforms",
    "role": "AI Intern",
    "title": "AI Intern at Jio Platforms",
    "description": "Implement AI-based personalization for content and telecom services.",
    "requirements": "Python, NLP techniques, recommendation engines.",
    "location": "Mumbai, Maharashtra",
    "start_date": "May 2025",
    "end_date": "July 2025",
    "duration": "3 months",
    "apply_link": "https://careers.jio.com"
},
{
    "company": "Microsoft India",
    "role": "Applied AI Intern",
    "title": "Applied AI Intern at Microsoft India",
    "description": "Collaborate on AI projects involving Azure AI and enterprise products.",
    "requirements": "Azure ML, Python, responsible AI practices.",
    "location": "Hyderabad, Telangana",
    "start_date": "May 2025",
    "end_date": "August 2025",
    "duration": "3 months",
    "apply_link": "https://careers.microsoft.com"
},
{
    "company": "Freshworks",
    "role": "AI Intern",
    "title": "AI Intern at Freshworks",
    "description": "Build AI chatbots and auto-routing systems for customer support.",
    "requirements": "Chatbot frameworks, NLU/NLP, Python.",
    "location": "Chennai, Tamil Nadu",
    "start_date": "June 2025",
    "end_date": "August 2025",
    "duration": "3 months",
    "apply_link": "https://www.freshworks.com/company/careers/"
},
{
    "company": "Samsung R&D",
    "role": "Machine Learning Intern",
    "title": "ML Intern at Samsung R&D Bangalore",
    "description": "Research and develop AI for mobile camera optimization and edge computing.",
    "requirements": "Computer Vision, TensorFlow Lite, Android AI SDKs.",
    "location": "Bangalore, Karnataka",
    "start_date": "May 2025",
    "end_date": "July 2025",
    "duration": "3 months",
    "apply_link": "https://research.samsung.com/careers"
}

        # You can easily add 10 more following this pattern.
    ]

    return render_template('ai_internships.html', internships=internships)
