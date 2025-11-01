from flask import render_template, Blueprint

sw_bp = Blueprint('sw', __name__)

@sw_bp.route('/software_engineer/internships')
def software_engineer_internships():
    internships = [
        {
            "company": "Google India",
            "role": "Software Engineering Intern",
            "title": "Software Engineer Intern at Google",
            "description": "Design, develop, and test software solutions for Google's platforms.",
            "requirements": "C++, Java, Python, Data Structures, Algorithms.",
            "location": "Hyderabad, Telangana",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://careers.google.com"
        },
        {
            "company": "Microsoft India",
            "role": "Software Intern",
            "title": "Software Engineer Intern at Microsoft",
            "description": "Collaborate with teams to build scalable software systems.",
            "requirements": "C#, .NET, React, SQL, OOP Concepts.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://careers.microsoft.com"
        },
        {
            "company": "NVIDIA",
            "role": "Software Engineering Intern",
            "title": "Intern - Software Engineering at NVIDIA",
            "description": "Build and optimize high-performance computing and AI software.",
            "requirements": "C++, Python, CUDA, Computer Architecture.",
            "location": "Pune, Maharashtra",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "4 months",
            "apply_link": "https://www.nvidia.com/en-in/about-nvidia/careers/"
        },
        {
            "company": "Samsung R&D",
            "role": "R&D Intern",
            "title": "Software Intern at Samsung Research",
            "description": "Work on mobile software features and device performance.",
            "requirements": "C/C++, Android, Git, Debugging skills.",
            "location": "Noida, Uttar Pradesh",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://research.samsung.com/careers"
        },
        {
            "company": "Cisco",
            "role": "Software Engineer Intern",
            "title": "Internship at Cisco India",
            "description": "Develop automation tools and scalable networking solutions.",
            "requirements": "Python, Java, Networking fundamentals, APIs.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://jobs.cisco.com"
        },
        {
            "company": "Adobe",
            "role": "Software Development Intern",
            "title": "SDE Intern at Adobe",
            "description": "Work on cloud-based products and AI integrations in Adobe tools.",
            "requirements": "Java, React, REST APIs, Docker.",
            "location": "Noida, Uttar Pradesh",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced"
        },
        {
            "company": "HackerRank",
            "role": "Software Engineer Intern",
            "title": "Intern at HackerRank",
            "description": "Work on platforms that help developers improve coding skills.",
            "requirements": "Ruby, React, SQL, Web Development.",
            "location": "Remote",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.hackerrank.com/careers"
        },
        {
            "company": "Tata Elxsi",
            "role": "Software Engineering Intern",
            "title": "Internship at Tata Elxsi",
            "description": "Assist in development for automotive and embedded systems.",
            "requirements": "C++, Embedded Systems, Linux, SDLC.",
            "location": "Trivandrum, Kerala",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.tataelxsi.com/careers"
        },
        {
            "company": "Oracle India",
            "role": "Software Development Intern",
            "title": "Software Engineer Intern at Oracle",
            "description": "Work on enterprise database tools and cloud-based SaaS applications.",
            "requirements": "Java, SQL, REST APIs, Cloud Concepts.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "3 months",
            "apply_link": "https://www.oracle.com/in/corporate/careers/"
        },
        {
            "company": "Intuit",
            "role": "Software Engineer Intern",
            "title": "Intuit Internship - Software Development",
            "description": "Contribute to FinTech applications like TurboTax and QuickBooks.",
            "requirements": "Node.js, React, AWS, CI/CD.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.intuit.com/careers/"
        },
        {
            "company": "Juspay",
            "role": "Software Developer Intern",
            "title": "Internship at Juspay",
            "description": "Work on scalable payment solutions and backend architecture.",
            "requirements": "Functional Programming (Haskell/Scala), Java, AWS.",
            "location": "Remote",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "3 months",
            "apply_link": "https://careers.juspay.in"
        },
        {
            "company": "Zeta",
            "role": "SDE Intern",
            "title": "Software Engineering Internship at Zeta",
            "description": "Build next-gen banking and card infrastructure services.",
            "requirements": "Java, Spring Boot, Microservices, Kafka.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://careers.zeta.tech"
        },
        {
            "company": "Publicis Sapient",
            "role": "Software Intern",
            "title": "Technology Intern at Publicis Sapient",
            "description": "Develop digital transformation solutions for global clients.",
            "requirements": "JavaScript, Angular/React, Java, Agile.",
            "location": "Gurugram, Haryana",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "2.5 months",
            "apply_link": "https://careers.publicissapient.com"
        },
        {
            "company": "KreditBee",
            "role": "Backend Developer Intern",
            "title": "Software Intern at KreditBee",
            "description": "Support loan management platforms and backend APIs.",
            "requirements": "Golang, Node.js, MongoDB, Redis.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://kreditbee.in/careers"
        },
        {
            "company": "Deloitte India",
            "role": "Tech Intern",
            "title": "Software Engineering Intern at Deloitte",
            "description": "Work with cloud and enterprise solution teams to deliver tech services.",
            "requirements": "Python, SQL, Power BI, Azure.",
            "location": "Hyderabad, Telangana",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://www2.deloitte.com/in/en/careers.html"
        },
        {
            "company": "L&T Infotech",
            "role": "Software Developer Intern",
            "title": "Internship at LTI Mindtree",
            "description": "Build software modules for enterprise and banking solutions.",
            "requirements": "Java, .NET, Oracle DB, REST APIs.",
            "location": "Chennai, Tamil Nadu",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "3 months",
            "apply_link": "https://careers.ltimindtree.com"
        }
    ]

    return render_template('sw_internships.html', internships=internships)
