from flask import Blueprint, render_template

ds_bp = Blueprint('ds', __name__)

@ds_bp.route('/data_scientist/internships')
def data_scientist_internships():

    internships = [
        {
            "company": "Mu Sigma",
            "role": "Data Science Intern",
            "title": "Data Science Intern at Mu Sigma",
            "description": "Work on business analytics and data modeling for Fortune 500 clients.",
            "requirements": "Strong Excel, SQL, Python, and business problem-solving mindset.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.mu-sigma.com/careers"
        },
        {
            "company": "Swiggy",
            "role": "Data Analyst Intern",
            "title": "Data Science Intern at Swiggy",
            "description": "Analyze customer behavior data to optimize delivery routes and pricing.",
            "requirements": "SQL, Tableau, Python, and basic statistics.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://careers.swiggy.com"
        },
        {
            "company": "Deloitte India",
            "role": "Data Science Intern",
            "title": "Data Science Intern at Deloitte India",
            "description": "Support analytics projects in financial services and risk modeling.",
            "requirements": "Python, machine learning basics, strong math/stats background.",
            "location": "Hyderabad, Telangana",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://www2.deloitte.com/in/en/careers.html"
        },
        {
            "company": "Zomato",
            "role": "Data Intern",
            "title": "Data Intern at Zomato",
            "description": "Predictive modeling for customer retention and food trends.",
            "requirements": "Numpy, Pandas, Matplotlib, classification models.",
            "location": "Gurgaon, Haryana",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.zomato.com/careers"
        },
        {
            "company": "Paytm",
            "role": "Data Science Intern",
            "title": "Data Science Intern at Paytm",
            "description": "Assist with fraud detection and customer segmentation models.",
            "requirements": "Scikit-learn, SQL, exploratory data analysis.",
            "location": "Noida, Uttar Pradesh",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://paytm.com/careers"
        },
        {
            "company": "EY India",
            "role": "Analytics Intern",
            "title": "Analytics Intern at EY India",
            "description": "Contribute to dashboard creation and predictive modeling for clients.",
            "requirements": "Power BI, Python, Excel, and regression models.",
            "location": "Mumbai, Maharashtra",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://www.ey.com/en_in/careers"
        },
        {
            "company": "Reliance Jio",
            "role": "Data Intern",
            "title": "Data Science Intern at Reliance Jio",
            "description": "Build recommendation engines and analyze usage data.",
            "requirements": "Python, collaborative filtering, time-series forecasting.",
            "location": "Mumbai, Maharashtra",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://careers.jio.com"
        },
        {
            "company": "Hike",
            "role": "Data Scientist Intern",
            "title": "Data Scientist Intern at Hike",
            "description": "User behavior modeling and content recommendation pipelines.",
            "requirements": "BigQuery, Airflow, machine learning pipelines.",
            "location": "Remote",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://hike.in/careers"
        },
        {
            "company": "UpGrad",
            "role": "Data Science Intern",
            "title": "Data Science Intern at UpGrad",
            "description": "Analyze learner journeys and predict course completion probabilities.",
            "requirements": "Python, data visualization, A/B testing.",
            "location": "Mumbai, Maharashtra",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.upgrad.com/about/careers/"
        },
        {
            "company": "Dream11",
            "role": "Data Intern",
            "title": "Data Science Intern at Dream11",
            "description": "Model user engagement and fantasy match predictions using ML.",
            "requirements": "Python, classification techniques, NumPy/Pandas.",
            "location": "Mumbai, Maharashtra",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://dream11careers.dreamsports.group"
        },
        {
            "company": "Mu Sigma",
            "role": "Data Science Intern",
            "title": "Data Science Intern at Mu Sigma",
            "description": "Work on business analytics and data modeling for Fortune 500 clients.",
            "requirements": "Strong Excel, SQL, Python, and business problem-solving mindset.",
            "location": "Bangalore, Karnataka",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.mu-sigma.com/careers"
        },
        {
            "company": "Swiggy",
            "role": "Data Analyst Intern",
            "title": "Data Science Intern at Swiggy",
            "description": "Analyze customer behavior data to optimize delivery routes and pricing.",
            "requirements": "SQL, Tableau, Python, and basic statistics.",
            "location": "Bangalore, Karnataka",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://careers.swiggy.com"
        },
        {
            "company": "DataCamp",
            "role": "Remote Data Science Intern",
            "title": "Remote Data Science Intern at DataCamp",
            "description": "Work on content analytics and predictive learning behavior models.",
            "requirements": "Python, Pandas, data storytelling, and remote collaboration skills.",
            "location": "Remote",
            "start_date": "May 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.datacamp.com/jobs"
        },
        {
            "company": "Kaggle",
            "role": "Community Data Intern",
            "title": "Remote Data Intern at Kaggle (Google)",
            "description": "Analyze notebook engagement and competition data for platform insights.",
            "requirements": "Strong data analysis, Jupyter, SQL, and Python.",
            "location": "Remote",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://www.kaggle.com/careers"
        },
        {
            "company": "Zomato",
            "role": "Data Intern",
            "title": "Data Intern at Zomato",
            "description": "Predictive modeling for customer retention and food trends.",
            "requirements": "Numpy, Pandas, Matplotlib, classification models.",
            "location": "Gurgaon, Haryana",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.zomato.com/careers"
        },
        {
            "company": "Paytm",
            "role": "Data Science Intern",
            "title": "Data Science Intern at Paytm",
            "description": "Assist with fraud detection and customer segmentation models.",
            "requirements": "Scikit-learn, SQL, exploratory data analysis.",
            "location": "Noida, Uttar Pradesh",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://paytm.com/careers"
        },
        {
            "company": "Hike",
            "role": "Data Scientist Intern",
            "title": "Remote Data Scientist Intern at Hike",
            "description": "User behavior modeling and content recommendation pipelines.",
            "requirements": "BigQuery, Airflow, machine learning pipelines.",
            "location": "Remote",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://hike.in/careers"
        },
        {
            "company": "UpGrad",
            "role": "Data Science Intern",
            "title": "Data Science Intern at UpGrad",
            "description": "Analyze learner journeys and predict course completion probabilities.",
            "requirements": "Python, data visualization, A/B testing.",
            "location": "Mumbai, Maharashtra",
            "start_date": "June 2025",
            "end_date": "August 2025",
            "duration": "3 months",
            "apply_link": "https://www.upgrad.com/about/careers/"
        },
        {
            "company": "Turing.com",
            "role": "Remote Data Science Intern",
            "title": "Remote Data Science Intern at Turing",
            "description": "Support AI talent matching with data-driven tools and algorithms.",
            "requirements": "Remote teamwork, ML fundamentals, SQL, and Git.",
            "location": "Remote",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://turing.com/careers"
        },
        {
            "company": "Dream11",
            "role": "Data Intern",
            "title": "Data Science Intern at Dream11",
            "description": "Model user engagement and fantasy match predictions using ML.",
            "requirements": "Python, classification techniques, NumPy/Pandas.",
            "location": "Mumbai, Maharashtra",
            "start_date": "May 2025",
            "end_date": "July 2025",
            "duration": "3 months",
            "apply_link": "https://dream11careers.dreamsports.group"
        }
    ]

    return render_template('ds_internships.html', internships=internships)
