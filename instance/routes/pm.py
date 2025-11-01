from flask import render_template, Blueprint

pm_bp = Blueprint('pm', __name__)

@pm_bp.route('/product_manager/internships')
def product_manager_internships():
    internships = [
        {
            "company": "Zomato",
            "role": "Product Intern",
            "title": "Product Intern at Zomato",
            "description": "Assist in defining product roadmaps and collaborate with engineers/designers to deliver seamless user experiences.",
            "requirements": "Strong analytical skills, SQL, product sense, and user empathy.",
            "location": "Gurgaon, Haryana",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.zomato.com/careers"
        },
        {
            "company": "Ola Cabs",
            "role": "APM Intern",
            "title": "Associate Product Manager Intern at Ola",
            "description": "Work on ride booking experiences and customer-facing features. Define KPIs and run experiments.",
            "requirements": "Excel/Google Sheets, analytics mindset, basic SQL.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://careers.olacabs.com"
        },
        {
            "company": "Razorpay",
            "role": "Product Intern",
            "title": "Product Strategy Intern at Razorpay",
            "description": "Conduct competitive research, support roadmap planning, and assist in feature rollouts.",
            "requirements": "SQL, Notion, communication, product documentation.",
            "location": "Remote",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "4 months",
            "apply_link": "https://razorpay.com/careers"
        },
        {
            "company": "Practo",
            "role": "Product Intern",
            "title": "Product Analyst Intern at Practo",
            "description": "Support healthcare platform decisions using product analytics and user feedback loops.",
            "requirements": "Data-driven mindset, Tableau, user interviews.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.practo.com/company/careers"
        },
        {
            "company": "Swiggy",
            "role": "Product Intern",
            "title": "Product Intern at Swiggy",
            "description": "Partner with design and tech teams to improve food delivery workflows.",
            "requirements": "Wireframing, A/B testing knowledge, analytical thinking.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://careers.swiggy.com"
        },
        {
            "company": "Dream11",
            "role": "Product Management Intern",
            "title": "Junior Product Manager Intern at Dream11",
            "description": "Define feature specs and improve sports engagement on mobile platforms.",
            "requirements": "Strong interest in sports & gaming, product documentation, JIRA.",
            "location": "Mumbai, Maharashtra",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.dream11.com/about/careers"
        },
        {
            "company": "Niyo",
            "role": "Product Growth Intern",
            "title": "Product & Growth Intern at Niyo",
            "description": "Analyze fintech product performance and optimize onboarding flows.",
            "requirements": "Excel, SQL, experimentation, product funnels.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://www.goniyo.com/careers"
        },
        {
            "company": "Vedantu",
            "role": "Product Intern",
            "title": "Product Intern at Vedantu",
            "description": "Collaborate with educators to launch tools for online learning, feedback, and progress tracking.",
            "requirements": "Edtech enthusiasm, wireframing (Figma), product research.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.vedantu.com/careers"
        },
        {
        "company": "CRED",
        "role": "Product Intern",
        "title": "Product Intern at CRED",
        "description": "Work with product and design to create unique member-first financial experiences.",
        "requirements": "Product thinking, customer obsession, Notion, Figma.",
        "location": "Bangalore, Karnataka",
        "start_date": "May 2025",
        "end_date": "July 2025",
        "duration": "3 months",
        "apply_link": "https://cred.club/careers"
    },
    {
        "company": "Unacademy",
        "role": "Product Analyst Intern",
        "title": "Product Intern at Unacademy",
        "description": "Identify user pain points, track KPIs, and help shape new learning experiences.",
        "requirements": "User empathy, analytics tools (Mixpanel, Amplitude), A/B testing.",
        "location": "Bangalore, Karnataka",
        "start_date": "June 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://unacademy.com/jobs"
    },
    {
        "company": "UpGrad",
        "role": "Product Management Intern",
        "title": "Product Intern at UpGrad",
        "description": "Assist in launching new learning programs and internal tooling.",
        "requirements": "Documentation, user research, collaboration, business logic.",
        "location": "Mumbai, Maharashtra",
        "start_date": "May 2025",
        "end_date": "July 2025",
        "duration": "3 months",
        "apply_link": "https://www.upgrad.com/careers"
    },
    {
        "company": "CoinSwitch",
        "role": "Product Intern",
        "title": "Crypto Product Intern at CoinSwitch",
        "description": "Support product initiatives in crypto investing, help define user journeys.",
        "requirements": "Crypto enthusiasm, SQL, wireframing, stakeholder collaboration.",
        "location": "Bangalore, Karnataka",
        "start_date": "June 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://coinswitch.co/careers"
    },
    {
        "company": "Ather Energy",
        "role": "Product Strategy Intern",
        "title": "Product Intern at Ather Energy",
        "description": "Work with EV teams to improve connected vehicle software experiences.",
        "requirements": "Tech curiosity, system thinking, analytical tools.",
        "location": "Bangalore, Karnataka",
        "start_date": "May 2025",
        "end_date": "August 2025",
        "duration": "4 months",
        "apply_link": "https://www.atherenergy.com/careers"
    },
    {
        "company": "Byju's",
        "role": "Product Management Intern",
        "title": "Product Intern at Byju's",
        "description": "Support interactive platform development and student analytics tools.",
        "requirements": "Edtech knowledge, Jira, strong communication.",
        "location": "Bangalore, Karnataka",
        "start_date": "June 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://byjus.com/careers"
    },
    {
        "company": "Bounce",
        "role": "Product Intern",
        "title": "Mobility Product Intern at Bounce",
        "description": "Improve app features related to vehicle booking and fleet tracking.",
        "requirements": "Google Analytics, user journey mapping, documentation.",
        "location": "Bangalore, Karnataka",
        "start_date": "May 2025",
        "end_date": "July 2025",
        "duration": "3 months",
        "apply_link": "https://bounceshare.com/careers"
    },
    {
        "company": "Dailyhunt",
        "role": "Product Analyst Intern",
        "title": "Product Intern at Dailyhunt",
        "description": "Support the recommendation engine and content personalization features.",
        "requirements": "Python (basic), metrics-driven thinking, product logging.",
        "location": "Bangalore, Karnataka",
        "start_date": "June 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://www.dailyhunt.in/careers"
    }
    ]

    return render_template('pm_internships.html', internships=internships)
