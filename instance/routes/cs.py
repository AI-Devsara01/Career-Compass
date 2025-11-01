from flask import render_template, Blueprint

cs_bp = Blueprint('cyber', __name__)

@cs_bp.route('/cybersecurity_analyst/internships')
def cybersecurity_internships():
    internships = [
        {
            "company": "Cisco India",
            "role": "Cybersecurity Intern",
            "title": "Cybersecurity Intern at Cisco",
            "description": "Assist in vulnerability management, firewall policy reviews, and incident response.",
            "requirements": "Networking fundamentals, Python, SIEM tools.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://jobs.cisco.com"
        },
        {
            "company": "TCS iON",
            "role": "Security Analyst Intern",
            "title": "Security Intern at TCS iON",
            "description": "Monitor and analyze logs, conduct threat intelligence research, and patch vulnerabilities.",
            "requirements": "Linux, OWASP, basic pen testing tools.",
            "location": "Mumbai, Maharashtra",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://www.tcs.com/careers"
        },
        {
            "company": "Check Point Software",
            "role": "Cybersecurity Research Intern",
            "title": "Remote Cybersecurity Intern at Check Point",
            "description": "Support malware analysis and help build secure architectures.",
            "requirements": "Python, malware analysis, reverse engineering basics.",
            "location": "Remote",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "3 months",
            "apply_link": "https://careers.checkpoint.com"
        },
        {
            "company": "Wipro",
            "role": "Cybersecurity Intern",
            "title": "Cybersecurity Intern at Wipro",
            "description": "Work on endpoint security, DLP solutions, and basic risk assessment tasks.",
            "requirements": "Security policies, antivirus tools, PowerShell/Bash.",
            "location": "Hyderabad, Telangana",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://careers.wipro.com"
        },
        {
            "company": "Palo Alto Networks",
            "role": "Security Automation Intern",
            "title": "Remote Security Intern at Palo Alto",
            "description": "Automate security policy validation and help secure cloud workloads.",
            "requirements": "Python, SOAR platforms, cloud security basics.",
            "location": "Remote",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://jobs.paloaltonetworks.com"
        },
                {
            "company": "EY (Ernst & Young)",
            "role": "Cybersecurity Analyst Intern",
            "title": "Cybersecurity Intern at EY",
            "description": "Assist in cybersecurity audits, risk assessment, and compliance checks for client infrastructure.",
            "requirements": "Information security basics, ISO/IEC 27001, risk management.",
            "location": "Gurgaon, Haryana",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.ey.com/en_in/careers"
        },
        {
            "company": "HCLTech",
            "role": "Cybersecurity Intern",
            "title": "Security Operations Intern at HCLTech",
            "description": "Support the SOC team in monitoring alerts, incident triaging, and reporting.",
            "requirements": "SIEM (Splunk/ELK), threat detection, basic IDS/IPS knowledge.",
            "location": "Noida, Uttar Pradesh",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://www.hcltech.com/careers"
        },
        {
            "company": "KPMG India",
            "role": "Cybersecurity Intern",
            "title": "Cyber Risk Intern at KPMG",
            "description": "Assist in cyber maturity assessments, data privacy reviews, and client-facing security reports.",
            "requirements": "GDPR, cyber governance, MS Excel, PowerPoint.",
            "location": "Mumbai, Maharashtra",
            "start_date": "June 2025",
            "end_date": "September 2025",
            "duration": "3 months",
            "apply_link": "https://home.kpmg/in/en/home/careers.html"
        },
        {
            "company": "CrowdStrike",
            "role": "Threat Intelligence Intern",
            "title": "Remote Threat Intelligence Intern at CrowdStrike",
            "description": "Contribute to tracking threat actor groups, gathering intel, and analyzing breaches.",
            "requirements": "Threat modeling, OSINT, scripting skills.",
            "location": "Remote",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.crowdstrike.com/careers/"
        },
        {
            "company": "Deloitte India",
            "role": "Cybersecurity Consultant Intern",
            "title": "Security Intern at Deloitte",
            "description": "Participate in red team-blue team simulations, audits, and client engagements.",
            "requirements": "NIST framework, risk analysis, Kali Linux basics.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://www2.deloitte.com/in/en/careers"
        },
        {
            "company": "Fortinet",
            "role": "Cybersecurity Intern",
            "title": "Network Security Intern at Fortinet",
            "description": "Assist with firewall configurations, rule base analysis, and threat prevention setup.",
            "requirements": "Network security, firewall basics, FortiOS (plus).",
            "location": "Pune, Maharashtra",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.fortinet.com/corporate/careers"
        },
        {
            "company": "Intel India",
            "role": "Cybersecurity Research Intern",
            "title": "Security Research Intern at Intel",
            "description": "Work with the product security team to identify and patch vulnerabilities in firmware and hardware.",
            "requirements": "C/C++, Secure boot, binary analysis.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.intel.com/content/www/us/en/jobs/jobs-at-intel.html"
        }

    ]

    return render_template('cs_internships.html', internships=internships)
