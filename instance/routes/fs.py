from flask import render_template, Blueprint

fs_bp = Blueprint('fs', __name__)

@fs_bp.route('/full_stack/internships')
def full_stack_internships():
    internships = [
    {
        "company": "TCS Digital",
        "role": "Full Stack Intern",
        "title": "Full Stack Developer Intern at TCS",
        "description": "Develop internal dashboards and REST APIs for enterprise tools.",
        "requirements": "JavaScript, Node.js, React, MongoDB.",
        "location": "Mumbai, Maharashtra",
        "start_date": "June 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://www.tcs.com/careers"
    },
    {
        "company": "Freshworks",
        "role": "Full Stack Engineering Intern",
        "title": "Engineering Intern at Freshworks",
        "description": "Work with product teams to build frontend and backend services.",
        "requirements": "Ruby on Rails, React, PostgreSQL.",
        "location": "Chennai, Tamil Nadu",
        "start_date": "May 2025",
        "end_date": "July 2025",
        "duration": "3 months",
        "apply_link": "https://www.freshworks.com/company/careers"
    },
    {
        "company": "Paytm",
        "role": "Product Intern",
        "title": "Full Stack Intern at Paytm",
        "description": "Contribute to mobile-first apps and payment gateway APIs.",
        "requirements": "Flutter/React Native, Node.js, MySQL.",
        "location": "Noida, Uttar Pradesh",
        "start_date": "June 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://paytm.com/careers"
    },
    {
        "company": "Zerodha",
        "role": "Tech Intern",
        "title": "Full Stack Web Intern at Zerodha",
        "description": "Enhance web interfaces for stock trading platforms.",
        "requirements": "Django, Vue.js, PostgreSQL.",
        "location": "Bangalore, Karnataka",
        "start_date": "June 2025",
        "end_date": "September 2025",
        "duration": "3 months",
        "apply_link": "https://zerodha.com/careers"
    },
    {
        "company": "Cred",
        "role": "Software Intern",
        "title": "Full Stack Intern at CRED",
        "description": "Join product engineering teams to build scalable features.",
        "requirements": "Next.js, GraphQL, TypeScript.",
        "location": "Bangalore, Karnataka",
        "start_date": "May 2025",
        "end_date": "August 2025",
        "duration": "4 months",
        "apply_link": "https://cred.club/careers"
    },
    {
        "company": "Flipkart",
        "role": "Software Development Intern",
        "title": "SDE Intern (Full Stack) at Flipkart",
        "description": "Develop scalable e-commerce modules and microservices.",
        "requirements": "Java, Spring Boot, React, Redis.",
        "location": "Bangalore, Karnataka",
        "start_date": "June 2025",
        "end_date": "September 2025",
        "duration": "3 months",
        "apply_link": "https://www.flipkartcareers.com"
    },
    {
        "company": "Zoho",
        "role": "Web Developer Intern",
        "title": "Full Stack Intern at Zoho",
        "description": "Build user-facing web apps and internal admin panels.",
        "requirements": "HTML/CSS, JS, PHP/Node.js, MySQL.",
        "location": "Chennai, Tamil Nadu",
        "start_date": "June 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://www.zoho.com/careers"
    },
    {
        "company": "Razorpay",
        "role": "Full Stack Intern",
        "title": "Engineering Intern at Razorpay",
        "description": "Work on checkout systems, backend APIs and user flows.",
        "requirements": "React, Go/Python, RESTful APIs.",
        "location": "Remote",
        "start_date": "May 2025",
        "end_date": "August 2025",
        "duration": "4 months",
        "apply_link": "https://razorpay.com/careers"
    },
    {
        "company": "Swiggy",
        "role": "Product Engineering Intern",
        "title": "Full Stack Intern at Swiggy",
        "description": "Develop order tracking UI and backend APIs for delivery teams.",
        "requirements": "JavaScript, React, Django/Flask.",
        "location": "Bangalore, Karnataka",
        "start_date": "May 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://careers.swiggy.com"
    },
    {
        "company": "Groww",
        "role": "Software Intern",
        "title": "Full Stack Developer Intern at Groww",
        "description": "Help build features for stock and mutual fund platforms.",
        "requirements": "Java, Angular, SQL, REST APIs.",
        "location": "Bangalore, Karnataka",
        "start_date": "June 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://groww.in/careers"
    },
    {
        "company": "Tech Mahindra",
        "role": "Web Dev Intern",
        "title": "Full Stack Intern at Tech Mahindra",
        "description": "Work on enterprise web apps and backend APIs.",
        "requirements": "Node.js, Angular, Express, MongoDB.",
        "location": "Hyderabad, Telangana",
        "start_date": "May 2025",
        "end_date": "July 2025",
        "duration": "3 months",
        "apply_link": "https://careers.techmahindra.com"
    },
    {
        "company": "InMobi",
        "role": "Engineering Intern",
        "title": "Full Stack Intern at InMobi",
        "description": "Build analytics dashboards and backends for data reporting.",
        "requirements": "React, Flask, PostgreSQL, Docker.",
        "location": "Bangalore, Karnataka",
        "start_date": "June 2025",
        "end_date": "September 2025",
        "duration": "3 months",
        "apply_link": "https://www.inmobi.com/company/careers"
    },
    {
        "company": "Meesho",
        "role": "Full Stack Intern",
        "title": "Software Intern at Meesho",
        "description": "Build features across the stack for social commerce platform.",
        "requirements": "React.js, Node.js, MongoDB, Redis.",
        "location": "Bangalore, Karnataka",
        "start_date": "May 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://careers.meesho.com"
    },
    {
        "company": "PhonePe",
        "role": "Software Development Intern",
        "title": "Full Stack Intern at PhonePe",
        "description": "Develop secure payment services and interactive UI components.",
        "requirements": "Java, Spring Boot, Angular, MySQL.",
        "location": "Bangalore, Karnataka",
        "start_date": "June 2025",
        "end_date": "September 2025",
        "duration": "4 months",
        "apply_link": "https://www.phonepe.com/careers"
    },
    {
        "company": "OYO",
        "role": "Engineering Intern",
        "title": "Full Stack Engineering Intern at OYO",
        "description": "Contribute to hotel booking platform, build admin tools and reports.",
        "requirements": "Python, Flask, React.js, PostgreSQL.",
        "location": "Gurugram, Haryana",
        "start_date": "May 2025",
        "end_date": "July 2025",
        "duration": "3 months",
        "apply_link": "https://www.oyorooms.com/careers"
    },
    {
        "company": "Urban Company",
        "role": "Tech Intern",
        "title": "Full Stack Developer Intern at Urban Company",
        "description": "Work with engineers to improve the customer and professional web portals.",
        "requirements": "Vue.js, Node.js, Firebase.",
        "location": "Gurugram, Haryana",
        "start_date": "June 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://www.urbancompany.com/careers"
    },
    {
        "company": "Navi Technologies",
        "role": "Backend + Frontend Intern",
        "title": "Full Stack Intern at Navi",
        "description": "Develop features for digital lending and insurance apps.",
        "requirements": "Kotlin/Java, React, SQL, REST APIs.",
        "location": "Bangalore, Karnataka",
        "start_date": "May 2025",
        "end_date": "August 2025",
        "duration": "4 months",
        "apply_link": "https://navi.com/careers"
    },
    {
        "company": "Delhivery",
        "role": "Web Intern",
        "title": "Full Stack Intern at Delhivery",
        "description": "Assist in logistics dashboards and delivery tracking services.",
        "requirements": "PHP/Laravel, JavaScript, PostgreSQL.",
        "location": "Gurugram, Haryana",
        "start_date": "June 2025",
        "end_date": "August 2025",
        "duration": "3 months",
        "apply_link": "https://www.delhivery.com/careers"
    },
    {
        "company": "Cogoport",
        "role": "Engineering Intern",
        "title": "Full Stack Developer Intern at Cogoport",
        "description": "Build digital logistics interfaces and backend APIs.",
        "requirements": "Node.js, Vue, MongoDB, Docker.",
        "location": "Mumbai, Maharashtra",
        "start_date": "May 2025",
        "end_date": "July 2025",
        "duration": "3 months",
        "apply_link": "https://www.cogoport.com/careers"
    },
    {
        "company": "Quikr",
        "role": "Full Stack Web Developer Intern",
        "title": "Web Dev Intern at Quikr",
        "description": "Modernize legacy systems and develop classified search UI.",
        "requirements": "JavaScript, Flask, MySQL.",
        "location": "Bangalore, Karnataka",
        "start_date": "June 2025",
        "end_date": "September 2025",
        "duration": "3 months",
        "apply_link": "https://www.quikr.com/jobs"
    }
]

    return render_template('fs_internships.html', internships=internships)