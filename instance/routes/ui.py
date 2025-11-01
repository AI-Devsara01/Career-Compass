# routes/uiux.py
from flask import render_template, Blueprint

ui_bp = Blueprint('uiux', __name__)

@ui_bp.route('/ui_ux_designer/internships')
def uiux_internships():
    internships = [
        {
            "company": "Adobe India",
            "role": "UI/UX Intern",
            "title": "UI/UX Design Intern at Adobe",
            "description": "Work on enhancing the user experience of Adobe Creative Cloud products.",
            "requirements": "Figma, Adobe XD, user research basics.",
            "location": "Noida, Uttar Pradesh",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://adobe.wd5.myworkdayjobs.com"
        },
        {
            "company": "Zeta (Directi)",
            "role": "Product Design Intern",
            "title": "Product Design Intern at Zeta",
            "description": "Collaborate with product teams to create intuitive mobile-first designs.",
            "requirements": "Figma, UX heuristics, mobile UI patterns.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "4 months",
            "apply_link": "https://careers.zeta.tech"
        },
        {
            "company": "Flipkart",
            "role": "UI Design Intern",
            "title": "UI Intern at Flipkart Design Team",
            "description": "Design UI elements for the e-commerce platform and contribute to the design system.",
            "requirements": "Sketch/Figma, UI kits, design tokens.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "3 months",
            "apply_link": "https://careers.flipkart.com"
        },
        {
            "company": "Freshworks",
            "role": "UX Research Intern",
            "title": "UX Research Intern at Freshworks",
            "description": "Conduct user interviews, usability tests, and analyze research data.",
            "requirements": "Qualitative research, empathy mapping, persona creation.",
            "location": "Chennai, Tamil Nadu",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://www.freshworks.com/company/careers"
        },
        {
            "company": "TCS Digital",
            "role": "Design Intern",
            "title": "UI/UX Intern at TCS Digital",
            "description": "Support cross-functional teams with wireframes, prototypes, and user flows.",
            "requirements": "Figma, wireframing tools, user-centered design.",
            "location": "Remote",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.tcs.com/careers"
        },
        {
            "company": "Razorpay",
            "role": "UX Design Intern",
            "title": "UX Intern at Razorpay",
            "description": "Collaborate on design audits and UX improvements for payment products.",
            "requirements": "Interaction design, usability principles, prototyping.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://razorpay.com/careers"
        },
        {
            "company": "Paytm",
            "role": "Design Intern",
            "title": "UI/UX Intern at Paytm",
            "description": "Create engaging designs and improve flows across mobile and web interfaces.",
            "requirements": "Design systems, typography, responsiveness.",
            "location": "Noida, Uttar Pradesh",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://paytm.com/careers"
        },
        {
            "company": "OYO",
            "role": "Product Design Intern",
            "title": "Design Intern at OYO Rooms",
            "description": "Work closely with PMs and engineers to deliver delightful user experiences.",
            "requirements": "UX flows, interaction design, wireframing tools.",
            "location": "Gurugram, Haryana",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://www.oyorooms.com/careers"
        },
        {
            "company": "CRED",
            "role": "Visual Design Intern",
            "title": "Visual Design Intern at CRED",
            "description": "Focus on motion design, typography, and UI elements for mobile banking products.",
            "requirements": "After Effects, typography, animation tools.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://cred.club/careers"
        },
        {
            "company": "Swiggy",
            "role": "Design Intern",
            "title": "Product Design Intern at Swiggy",
            "description": "Improve consumer and delivery partner experiences with design experiments.",
            "requirements": "Figma, user feedback analysis, micro-interactions.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://careers.swiggy.com"
        },
                {
            "company": "MakeMyTrip",
            "role": "UI/UX Design Intern",
            "title": "Design Intern at MakeMyTrip",
            "description": "Assist with redesigning travel booking interfaces for improved usability.",
            "requirements": "Figma, travel UX trends, user personas.",
            "location": "Gurugram, Haryana",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.makemytrip.com/careers"
        },
        {
            "company": "Urban Company",
            "role": "Product Design Intern",
            "title": "Product Design Intern at Urban Company",
            "description": "Design flows for service providers and improve booking experience.",
            "requirements": "Wireframes, user research, visual design.",
            "location": "Gurugram, Haryana",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.urbancompany.com/careers"
        },
        {
            "company": "BYJU'S",
            "role": "Design Intern",
            "title": "UI/UX Intern at BYJU'S",
            "description": "Support learning app interfaces with engaging and kid-friendly designs.",
            "requirements": "Illustration, design for education, mobile design.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "4 months",
            "apply_link": "https://byjus.com/careers"
        },
        {
            "company": "Nykaa",
            "role": "Visual Design Intern",
            "title": "UI Intern at Nykaa",
            "description": "Work on high-conversion UI for beauty and fashion products across devices.",
            "requirements": "Color theory, responsive UI, Figma.",
            "location": "Mumbai, Maharashtra",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://careers.nykaa.com"
        },
        {
            "company": "Tata Digital",
            "role": "Design Intern",
            "title": "UX Intern at Tata Digital",
            "description": "Research and prototype solutions for Tata Neu app users.",
            "requirements": "UX writing, design thinking, mobile-first design.",
            "location": "Mumbai, Maharashtra",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.tatadigital.com/careers"
        },
        {
            "company": "PhonePe",
            "role": "Interaction Design Intern",
            "title": "UI/UX Intern at PhonePe",
            "description": "Design seamless digital payment experiences and iterate based on A/B testing.",
            "requirements": "A/B testing, microinteractions, UI audits.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.phonepe.com/careers"
        },
        {
            "company": "Meesho",
            "role": "Design Intern",
            "title": "UX Research & UI Design Intern at Meesho",
            "description": "Combine research and interface design for B2B and B2C tools.",
            "requirements": "Usability testing, heuristic evaluation, interface mockups.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "4 months",
            "apply_link": "https://meesho.io/careers"
        },
        {
            "company": "Cogoport",
            "role": "UX Design Intern",
            "title": "Product UX Intern at Cogoport",
            "description": "Design logistics and freight management dashboards with intuitive UX.",
            "requirements": "Dashboard design, B2B UX, prototyping tools.",
            "location": "Remote",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.cogoport.com/careers"
        }

    ]

    return render_template('uiux_internships.html', internships=internships)
