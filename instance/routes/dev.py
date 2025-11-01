# routes/devops.py
from flask import render_template, Blueprint

dev_bp = Blueprint('devops', __name__)

@dev_bp.route('/devops_engineer/internships')
def devops_internships():
    internships = [
        {
            "company": "Amazon Web Services (AWS)",
            "role": "DevOps Intern",
            "title": "AWS DevOps Intern",
            "description": "Assist with CI/CD pipeline setups and automate infrastructure provisioning.",
            "requirements": "AWS, Docker, Jenkins, Python/Bash.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://aws.amazon.jobs"
        },
        {
            "company": "Infosys",
            "role": "DevOps Intern",
            "title": "DevOps Intern at Infosys",
            "description": "Support monitoring, release automation, and infrastructure as code implementations.",
            "requirements": "Linux, Ansible, Git, Jenkins.",
            "location": "Mysuru, Karnataka",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://careers.infosys.com"
        },
        {
            "company": "Zoho Corporation",
            "role": "Cloud DevOps Intern",
            "title": "Cloud DevOps Intern at Zoho",
            "description": "Manage deployment workflows and monitor application uptime and reliability.",
            "requirements": "Docker, Kubernetes, shell scripting.",
            "location": "Chennai, Tamil Nadu",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.zoho.com/careers"
        },
        {
            "company": "Tata Elxsi",
            "role": "Infrastructure Automation Intern",
            "title": "DevOps Intern at Tata Elxsi",
            "description": "Write automation scripts and support DevOps engineers in maintaining cloud infra.",
            "requirements": "Terraform, Python, Linux basics.",
            "location": "Pune, Maharashtra",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.tataelxsi.com/careers"
        },
        {
            "company": "Capgemini",
            "role": "DevOps Tools Intern",
            "title": "Remote DevOps Intern at Capgemini",
            "description": "Contribute to CI/CD pipelines and help manage development environments.",
            "requirements": "GitLab CI, Docker, basic cloud (AWS/GCP/Azure).",
            "location": "Remote",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "3 months",
            "apply_link": "https://www.capgemini.com/careers"
        },
                {
            "company": "Google Cloud India",
            "role": "Site Reliability Engineering Intern",
            "title": "SRE Intern at Google Cloud",
            "description": "Help ensure system reliability and availability of cloud-native apps.",
            "requirements": "Python/Go, Linux internals, Prometheus, Kubernetes.",
            "location": "Hyderabad, Telangana",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "4 months",
            "apply_link": "https://careers.google.com"
        },
        {
            "company": "Red Hat",
            "role": "DevOps Automation Intern",
            "title": "DevOps Intern at Red Hat",
            "description": "Automate deployment pipelines and participate in open-source tooling improvements.",
            "requirements": "Ansible, Jenkins, Bash, Git.",
            "location": "Pune, Maharashtra",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "4 months",
            "apply_link": "https://www.redhat.com/en/jobs"
        },
        {
            "company": "Reliance Jio",
            "role": "Cloud DevOps Intern",
            "title": "Cloud DevOps Intern at Jio Platforms",
            "description": "Support microservices deployment and monitor system health in cloud environments.",
            "requirements": "Kubernetes, Docker, ELK Stack.",
            "location": "Mumbai, Maharashtra",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://careers.jio.com"
        },
        {
            "company": "HCL Technologies",
            "role": "DevOps & Monitoring Intern",
            "title": "DevOps Monitoring Intern at HCL",
            "description": "Set up logging and observability using tools like Grafana and Prometheus.",
            "requirements": "Grafana, Linux, Bash/Python.",
            "location": "Noida, Uttar Pradesh",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.hcltech.com/careers"
        },
        {
            "company": "Mindtree",
            "role": "CI/CD Engineering Intern",
            "title": "DevOps Intern at Mindtree",
            "description": "Help build and maintain CI/CD systems and improve code delivery pipelines.",
            "requirements": "GitHub Actions, Jenkins, Docker.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.ltimindtree.com/careers"
        },
        {
            "company": "Dell Technologies",
            "role": "DevOps Intern",
            "title": "DevOps Intern at Dell",
            "description": "Assist in container orchestration and automated infrastructure testing.",
            "requirements": "Kubernetes, Python, Terraform, GitLab CI/CD.",
            "location": "Remote",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "3 months",
            "apply_link": "https://jobs.dell.com"
        },
        {
            "company": "Siemens",
            "role": "DevOps Process Intern",
            "title": "DevOps Process Intern at Siemens",
            "description": "Support the integration of DevOps practices into traditional engineering workflows.",
            "requirements": "Azure DevOps, scripting, version control systems.",
            "location": "Gurugram, Haryana",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://new.siemens.com/in/en/company/jobs.html"
        },
        {
            "company": "IBM",
            "role": "Automation & Infrastructure Intern",
            "title": "DevOps Intern at IBM India",
            "description": "Work on cloud automation tools and contribute to hybrid cloud infrastructure.",
            "requirements": "IBM Cloud, Python, Terraform, DevOps tools.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.ibm.com/in-en/employment"
        }

    ]

    return render_template('dev_internships.html', internships=internships)
