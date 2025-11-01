from flask import render_template,Blueprint
ce_bp = Blueprint('ce', __name__)

@ce_bp.route('/cloud_engineer/internships')
def cloud_engineer_internships():
    internships = [
        {
            "company": "Google Cloud India",
            "role": "Cloud Engineering Intern",
            "title": "Cloud Engineering Intern at Google Cloud",
            "description": "Work with cloud infrastructure, automate deployments, and monitor resources across GCP.",
            "requirements": "GCP, Python/Shell scripting, Kubernetes, CI/CD tools.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://careers.google.com"
        },
        {
            "company": "Infosys",
            "role": "Cloud Intern",
            "title": "Cloud Intern at Infosys",
            "description": "Support cloud migration projects and cloud-native development initiatives.",
            "requirements": "AWS, Docker, Terraform, strong Linux fundamentals.",
            "location": "Hyderabad, Telangana",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://careers.infosys.com"
        },
        {
            "company": "Microsoft India",
            "role": "Azure Intern",
            "title": "Cloud Intern at Microsoft (Azure)",
            "description": "Assist Azure team in automating cloud operations, managing resources, and optimizing cost.",
            "requirements": "Azure CLI, ARM templates, Python, DevOps practices.",
            "location": "Remote",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://careers.microsoft.com"
        },
        {
            "company": "Zoho",
            "role": "Cloud Engineering Intern",
            "title": "Cloud Engineering Intern at Zoho",
            "description": "Develop and monitor backend services on private and public clouds.",
            "requirements": "Linux, AWS basics, networking, scripting skills.",
            "location": "Chennai, Tamil Nadu",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.zoho.com/careers/"
        },
        {
            "company": "Scaler",
            "role": "Remote Cloud Intern",
            "title": "Remote Cloud Intern at Scaler",
            "description": "Contribute to building infrastructure as code and automating environments.",
            "requirements": "Terraform, AWS, Jenkins, YAML, GitHub Actions.",
            "location": "Remote",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.scaler.com/careers"
        },
                {
            "company": "TCS Digital",
            "role": "Cloud Engineering Intern",
            "title": "Cloud Intern at TCS Digital",
            "description": "Work on hybrid cloud environments and support deployment automation across platforms.",
            "requirements": "AWS/Azure, CI/CD pipelines, Git, basic cloud security.",
            "location": "Pune, Maharashtra",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "3 months",
            "apply_link": "https://www.tcs.com/careers"
        },
        {
            "company": "Razorpay",
            "role": "DevOps & Cloud Intern",
            "title": "Cloud Infrastructure Intern at Razorpay",
            "description": "Help manage cloud infra scalability, automation scripts, and monitoring dashboards.",
            "requirements": "Python, AWS, Prometheus, Docker, CloudWatch.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://razorpay.com/careers/"
        },
        {
            "company": "Nutanix India",
            "role": "Cloud Intern",
            "title": "Remote Cloud Intern at Nutanix",
            "description": "Support private/hybrid cloud solutions and conduct performance testing.",
            "requirements": "Kubernetes, shell scripting, REST APIs, virtualization basics.",
            "location": "Remote",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.nutanix.com/company/careers"
        },
        {
            "company": "RedHat",
            "role": "Cloud DevOps Intern",
            "title": "Remote Cloud DevOps Intern at RedHat",
            "description": "Contribute to automation workflows using Ansible and monitor CI pipelines.",
            "requirements": "Ansible, OpenShift, Linux admin, YAML scripting.",
            "location": "Remote",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.redhat.com/en/jobs"
        },
        {
            "company": "Capgemini",
            "role": "Cloud Intern",
            "title": "Cloud Intern at Capgemini",
            "description": "Work on enterprise cloud migrations and write deployment scripts.",
            "requirements": "AWS CLI, Python, Jenkins, Docker, Git.",
            "location": "Noida, Uttar Pradesh",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://www.capgemini.com/in-en/careers/"
        }

    ]

    return render_template('ce_internships.html', internships=internships)
