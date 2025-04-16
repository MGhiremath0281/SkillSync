from pdfminer.high_level import extract_text
from docx import Document

def extract_keywords(text):
    skills_list = ['Python', 'Machine Learning', 'Data Science', 'Flask', 'SQL', 'Pandas']
    found_skills = [skill for skill in skills_list if skill.lower() in text.lower()]
    return found_skills

def extract_text_from_docx(file):
    doc = Document(file)
    return '\n'.join([para.text for para in doc.paragraphs])

def extract_skills(file):
    filename = file.filename.lower()
    
    if filename.endswith('.pdf'):
        text = extract_text(file.stream)  # Read from in-memory stream
    elif filename.endswith('.txt'):
        text = file.read().decode('utf-8')  # Decode bytes to string
    elif filename.endswith('.docx'):
        text = extract_text_from_docx(file)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF, TXT, or DOCX file.")
    
    return extract_keywords(text)
