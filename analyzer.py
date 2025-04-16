def analyze_skills(job, resume_skills, db):
    # Assume job.skills is already a list of skills (not a string)
    job_skills = [s.strip().lower() for s in job.skills if isinstance(s, str)]
    resume_skills = [s.lower() for s in resume_skills]

    # Skill comparison
    matched_skills = set(resume_skills).intersection(job_skills)
    missing_skills = set(job_skills).difference(matched_skills)

    # Match percentage calculation
    match_percent = int((len(matched_skills) / len(job_skills)) * 100) if job_skills else 0

    # Fetch recommended courses based on job ID
    recommended_courses = (
        db.query(job.__class__.courses.property.mapper.class_)
        .filter_by(job_id=job.id)
        .all()
    )

    return match_percent, list(missing_skills), recommended_courses
