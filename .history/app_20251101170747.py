from flask import Flask, render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import pandas as pd
import os
import traceback

# Import your blueprints and resume analyzer
from instance.routes.resume import analyze_resume 
from instance.routes.ai import ai_bp 
from instance.routes.ds import ds_bp 
from instance.routes.cs import cs_bp 
from instance.routes.ce import ce_bp 
from instance.routes.dev import dev_bp
from instance.routes.ui import ui_bp
from instance.routes.fs import fs_bp
from instance.routes.bc import bc_bp
from instance.routes.sw import sw_bp
from instance.routes.pm import pm_bp

# Flask App instance
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Register blueprints
app.register_blueprint(ai_bp)
app.register_blueprint(ds_bp)
app.register_blueprint(ce_bp)
app.register_blueprint(cs_bp)
app.register_blueprint(dev_bp)
app.register_blueprint(ui_bp)
app.register_blueprint(fs_bp)
app.register_blueprint(bc_bp)
app.register_blueprint(sw_bp)
app.register_blueprint(pm_bp)

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['TRAP_HTTP_EXCEPTIONS'] = True
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure uploads folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize DB
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Serve favicon.ico
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

# Load dataset utility function
def load_dataset(role):
    csv_path = os.path.join('data', f'{role}.csv')
    if not os.path.exists(csv_path):
        print(f"❌ Dataset file not found for role: {role}")
        return []
    df = pd.read_csv(csv_path)
    return df.to_dict(orient='records')

# Single /view/<role> route with template mapping
@app.route('/view/<role>')
def view_role(role):
    allowed_roles = {
        "ai_engineer", "data_scientist", "software_engineer", "product_manager",
        "cloud_engineer", "full_stack_developer", "blockchain_developer",
        "devops_engineer", "cybersecurity_analyst", "ui_ux_designer"
    }
    
    if role not in allowed_roles:
        abort(404)

    try:
        # Load dataset from CSV
        csv_path = os.path.join('data', f'{role}.csv')
        if not os.path.exists(csv_path):
            flash(f"Dataset not found for {role.replace('_', ' ').title()}", "error")
            return redirect(url_for('home'))
        
        # Read CSV and convert to list of dictionaries
        df = pd.read_csv(csv_path)
        dataset = df.where(pd.notnull(df), None).to_dict('records')
        
        # Debug print to check data
        print(f"Loaded {len(dataset)} records for {role}")
        if dataset:
            print("Sample record:", dataset[0])
        
        return render_template('roadmap.html', dataset=dataset, role=role.replace('_', ' ').title())
    
    except Exception as e:
        print(f"Error loading dataset: {str(e)}")
        flash("Error loading roadmap data", "error")
        return redirect(url_for('home'))
# Main site routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please log in.', 'danger')
            return redirect(url_for('login'))

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Signup successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password. Try again.', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html', user_name=session['user_name'])
    flash('Please log in first.', 'warning')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/ai-engineer/internships')
def ai_internships():
    return render_template('ai_internships.html')

@app.route('/soft_skills')
def softskills():
    return render_template('soft_skills.html')

@app.route('/roles')
def view_roles():
    return render_template('roles.html')

@app.route('/internships')
def internships():
    return render_template('internships.html')

@app.route('/mock_interview')
def mock_interview():
    return render_template('mock_interview.html')

@app.route('/modules')
def modules():
    module_name = request.args.get('module', 'default')
    return render_template('modules.html', module=module_name)

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')  
    # Also add this route for direct access
@app.route('/chat')
def alt_chat():
    return render_template('chat.html'  )

@app.route('/res', methods=['GET', 'POST'])
def res():
    if request.method == 'POST':
        if 'resume' not in request.files:
            return render_template('res.html', error='No file part in the request.')

        file = request.files['resume']
        if file.filename == '':
            return render_template('res.html', error='No file selected.')

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            result = analyze_resume(filepath)
            if 'error' in result:
                return render_template('res.html', error=result['error'])

            return render_template('res.html', result=result)
        except Exception as e:
            return render_template('res.html', error=f"Error analyzing resume: {str(e)}")
            

    return render_template('res.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return render_template('resume.html', error='No file uploaded.')

    file = request.files['resume']
    if file.filename == '':
        return render_template('resume.html', error='No selected file.')

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    ats_score, results = analyze_resume(filepath)

    return render_template('resume.html', ats_score=ats_score, results=results)

# Mock interview per role
@app.route('/mock_interview/<role>')
def mock_interview_detail(role):
    valid_templates = {
        "ai_engineer": "mi_aiml.html",
        "data_scientist": "mi_ds.html",
        "cloud_engineer": "mi_cloud.html",
        "cybersecurity_analyst": "mi_cyber.html",
        "full_stack_developer": "mi_fullstack.html",
        "devops_engineer": "mi_devops.html",
        "blockchain_developer": "mi_blockchain.html",
        "uiux_designer": "mi_uiux.html",
        "product_manager": "mi_pm.html",
        "software_engineer": "mi_software.html"
    }

    template_name = valid_templates.get(role)
    if not template_name:
        return "Invalid role. Mock interview page not found.", 404

    return render_template(template_name, role=role.replace('_', ' ').title())

# Global error handler
@app.errorhandler(Exception)
def handle_exception(e):
    error_details = traceback.format_exc()
    print(error_details)
    return render_template('error.html', error=error_details), 500

# Create tables before first request
with app.app_context():
    db.create_all()

# Run app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000, use_reloader=False)
