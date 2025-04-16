# SkillSync – Resume Skill Gap Analyzer

**SkillSync** is a smart web app that helps job seekers identify the skill gap between their resume and the requirements of a chosen job role.

---

## 🧠 How It Works

1. **Upload Resume**: You upload your resume in PDF or DOCX format.
2. **Select Job Role**: Choose a job title from the dropdown (e.g., Data Scientist, Web Developer).
3. **Skill Extraction**: The app parses your resume using NLP and extracts your skills.
4. **Gap Analysis**: It compares your skills with the required skills for the selected job role.
5. **Result**: It displays:
   - ✅ Skills you already have
   - ❌ Skills you are missing

---

## 🔧 Tech Stack Used

- **Frontend**: HTML, CSS (Jinja templates with Flask)
- **Backend**: Python (Flask Framework)
- **NLP & Parsing**:
  - spaCy – for skill extraction
  - pdfplumber, python-docx – to read resume files
- **Database**: PostgreSQL with SQLAlchemy

---

## 📦 How to Clone and Run

### 1. Clone the Repository

```bash
git clone https://github.com/MGhiremath0281/SkillSync.git
cd SkillSync
