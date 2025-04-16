from flask import Flask, render_template, request
from database import SessionLocal
from models import Job, Course
from resume_parser import extract_skills  # Import from your resume_parser.py
from analyzer import analyze_skills

app = Flask(__name__)
db = SessionLocal()

@app.route('/')
def index():
    jobs = db.query(Job).all()
    return render_template('index.html', jobs=jobs)

@app.route('/analyze', methods=['POST'])
def analyze():
    job_id = request.form['job']
    resume = request.files['resume']
    job = db.query(Job).filter(Job.id == job_id).first()

    # Extract skills from the uploaded resume using our function
    extracted_skills = extract_skills(resume)

    # Compare with job and get suggestions
    match_percent, missing_skills, recommended_courses = analyze_skills(job, extracted_skills, db)

    return render_template('results.html',
                           job_title=job.title,
                           match_percent=match_percent,
                           missing_skills=missing_skills,
                           recommended_courses=recommended_courses)

if __name__ == '__main__':
    app.run(debug=True)
