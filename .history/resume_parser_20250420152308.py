from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import pandas as pd
import os
import traceback
import ast

# 🔹 Blueprints
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

# 🔹 Resume logic
from resume_parser import extract_text, recommend_role

# ✅ Initialize App
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# ✅ Register Blueprints
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

# ✅ Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# ✅ DB Init
db = SQLAlchemy(app)

# ✅ Dataset Loader
def load_dataset(role):
    # Map each role to its CSV filename
    role_map = {
        'data_scientist': 'data_scientist.csv',
        'ai_engineer': 'ai_engineer.csv',
        'cloud_engineer': 'cloud_engineer.csv',
        'full_stack_developer': 'full_stack_developer.csv',
        'cybersecurity_analyst': 'cyber_sec.csv',
        'ui_ux_designer': 'uiux.csv',
        'devops_engineer': 'devops.csv',
        'product_manager': 'pm.csv',
        'blockchain_developer': 'bc.csv',
        'software_engineer': 'software_engineer.csv'
    }

    filename = role_map.get(role)
    if not filename:
        print(f"[WARNING] Role '{role}' not found in role_map.")
        return []

    filepath = os.path.join('data', filename)
    print(f"[INFO] Loading dataset from: {filepath}")

    if not os.path.exists(filepath):
        print(f"[ERROR] File not found: {filepath}")
        return []

    # Load the CSV file and parse it
    df = pd.read_csv(filepath)
    
    # Safely parse list-like string columns
    for col in ['Project', 'Interview Questions']:
        if col in df.columns:
            df[col] = df[col].apply(
                lambda x: ast.literal_eval(x) if pd.notna(x) and isinstance(x, str) and x.startswith('[') and x.endswith(']')
                else [x] if pd.notna(x) else []
            )

    for index, row in df.iterrows():
        print(f"Project: {row['Project']}")
        for question in row['Interview Questions']:
            print(question)
            print('-' * 50)  # Separator between each project
    return df.to_dict(orient='records')

# ✅ Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# ✅ Routes
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
        db.session.add(User(name=name, email=email, password=hashed_password))
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
        flash('Invalid credentials.', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html', user_name=session['user_name'])
    flash('Please log in first.', 'warning')
    return redirect(url_for('login'))

@app.route('/internships')
def internships():
    return render_template('internships.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/view/<role>')
def view_role(role):
    try:
        # Load the dataset for the role
        dataset = load_dataset(role)

        if not dataset:
            return f"Error loading data for role: {role}", 404

        # Map each role to its specific roadmap template
        role_templates = {
            "data_scientist": "roadmapds.html",
            "ai_engineer": "roadmap.html",
            "cloud_engineer": "roadmapce.html",
            "full_stack_developer": "roadmapfs.html",
            "cybersecurity_analyst": "roadmapcs.html",
            "software_engineer": "roadmapse.html",
            "devops_engineer":"roadmapde.html",
            "blockchain_developer":"roadmapbc.html",
            "ui_ux_designer":"roadmapuiux.html",
            "product_manager":"roadmappm.html",
        }

        # Get the template or return 404 if role is not recognized
        template = role_templates.get(role)
        if not template:
            return render_template("404.html"), 404  # Optional: Add a custom 404 template
        
        return render_template(template, dataset=dataset, role=role)

    except Exception as e:
        print(f"[DEBUG] Role requested: {role}")
        print(f"[DEBUG] Dataset: {dataset}")
        return f"[ERROR] Failed to load dataset for role '{role}': {e}", 500

@app.route('/resume', methods=['GET'])
def resume_upload():
    return render_template('resume.html')

@app.route('/resume', methods=['POST'])
def parse_resume():
    if 'resume' not in request.files:
        flash("No file uploaded", "warning")
        return redirect(request.url)

    file = request.files['resume']
    if file.filename == '':
        flash("No selected file", "warning")
        return redirect(request.url)

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    resume_text = extract_text(filepath)

    if not resume_text.strip():
        flash("Could not read text from the resume. Please upload a clearer file.", "danger")
        return redirect(request.url)

    analysis = recommend_role(resume_text)
    role_slug = analysis.get("role_slug", "")

    return render_template("resume.html", role=role_slug, analysis=analysis)

@app.route('/roles')
def view_roles():
    return render_template('roles.html')

@app.route('/soft_skills')
def softskills():
    return render_template('soft_skills.html')

@app.route('/modules')
def modules():
    module_name = request.args.get('module', 'default')
    templates = {
        'communication': 'modules.html',
        'problem-solving': 'problem-solving.html',
        'time-management': 'tm.html',
        'emotional-intelligence': 'ei.html',
        'leadership': 'leadership.html'
    }
    return render_template(templates.get(module_name, 'default.html'))

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

# ✅ Global Error Handler
@app.errorhandler(Exception)
def handle_exception(e):
    print(traceback.format_exc())
    return render_template('error.html', error=str(e)), 500

@app.route('/mock_interview')
def mock_interview():
    return render_template('mock_interview.html')

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

# ✅ DB Init
with app.app_context():
    db.create_all()