# routes.py

from flask import Blueprint, render_template, session, redirect, url_for

ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/ai-engineer/internships')
def ai_internships():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Mock Interview Check
    mock_done = session.get('ai_mock_completed', False)

    if not mock_done:
        return render_template('complete_mock.html')  # Add a template prompting mock completion

    # Internship Data (from Python, not CSV)
    internships = [
        {"company": "OpenAI", "role": "AI Research Intern", "description": "Work on cutting-edge AI models.", "apply_link": "https://openai.com/careers"},
        {"company": "Google", "role": "AI Intern", "description": "Contribute to ML pipelines at scale.", "apply_link": "https://careers.google.com"},
        {"company": "NVIDIA", "role": "AI Software Intern", "description": "Optimize deep learning frameworks.", "apply_link": "https://nvidia.com/careers"},
        {"company": "Meta", "role": "AI Systems Intern", "description": "Work on LLM infrastructure.", "apply_link": "https://www.metacareers.com"},
        {"company": "Amazon", "role": "Applied Scientist Intern", "description": "Build real-world ML solutions.", "apply_link": "https://www.amazon.jobs"},
        {"company": "Adobe", "role": "AI Research Intern", "description": "Develop ML models for design tools.", "apply_link": "https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced"},
        {"company": "IBM", "role": "Watson AI Intern", "description": "Work on IBM Watson solutions.", "apply_link": "https://www.ibm.com/careers"},
        {"company": "LinkedIn", "role": "AI Product Intern", "description": "Enhance job recommendation systems.", "apply_link": "https://careers.linkedin.com"},
        {"company": "TCS", "role": "AI Research Intern", "description": "Explore NLP solutions at scale.", "apply_link": "https://www.tcs.com/careers"},
        {"company": "Wipro", "role": "AI Engineer Intern", "description": "Support AI-driven automation.", "apply_link": "https://careers.wipro.com"},
        {"company": "Zoho", "role": "ML Intern", "description": "Work on Zoho’s ML engine.", "apply_link": "https://www.zoho.com/careers"},
        {"company": "SAP", "role": "AI Business Intern", "description": "Design intelligent enterprise apps.", "apply_link": "https://www.sap.com/about/careers.html"},
        {"company": "Intel", "role": "AI R&D Intern", "description": "Build AI solutions for chip-level optimization.", "apply_link": "https://jobs.intel.com"},
        {"company": "Salesforce", "role": "Einstein AI Intern", "description": "Contribute to the Einstein platform.", "apply_link": "https://www.salesforce.com/company/careers"},
        {"company": "Apple", "role": "AI/ML Intern", "description": "Innovate in Siri and Vision.", "apply_link": "https://jobs.apple.com"},
        {"company": "CureMetrix", "role": "Medical AI Intern", "description": "Work on AI-powered diagnostics.", "apply_link": "https://www.curemetrix.com"},
        {"company": "Samsung", "role": "AI Software Intern", "description": "Join the AI Research Lab.", "apply_link": "https://research.samsung.com/careers"},
        {"company": "Qualcomm", "role": "Neural Networks Intern", "description": "Develop AI for mobile chips.", "apply_link": "https://www.qualcomm.com/careers"},
        {"company": "Hugging Face", "role": "NLP Intern", "description": "Contribute to Transformers library.", "apply_link": "https://huggingface.co"},
        {"company": "Anthropic", "role": "AI Alignment Intern", "description": "Work on AI safety research.", "apply_link": "https://www.anthropic.com"},
    ]

    # Top Internship Portals
    portals = [
        {"name": "Internshala", "desc": "India's most popular internship platform with direct applications.", "link": "https://internshala.com"},
        {"name": "LinkedIn", "desc": "Find internships with filters, recruiter reachouts & referrals.", "link": "https://www.linkedin.com/jobs"},
        {"name": "Naukri.com", "desc": "One of India’s largest job/internship boards.", "link": "https://www.naukri.com"},
        {"name": "AngelList Talent (Wellfound)", "desc": "Startup internships with rapid hiring cycles.", "link": "https://wellfound.com"},
        {"name": "Simplify Jobs", "desc": "Fast application to tech roles with autofill & tracking.", "link": "https://simplify.jobs"},
    ]

    return render_template('ai_internships.html', internships=internships, portals=portals, mock_done=mock_done)
