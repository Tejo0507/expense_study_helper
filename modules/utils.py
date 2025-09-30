import re
from datetime import datetime

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\d+', '', text)
    return text.strip()

def parse_exam_dates(exams_text: str) -> dict:
    exams = {}
    lines = [line.strip() for line in exams_text.split('\n') if line.strip()]
    for line in lines:
        try:
            subj, date_str = line.split(":")
            date_obj = datetime.strptime(date_str.strip(), "%Y-%m-%d")
            exams[subj.strip()] = date_obj
        except ValueError:
            raise ValueError(f"Invalid exam date format in line: {line}")
    return exams

def validate_subjects(subjects_list: list):
    if not all(isinstance(s, str) for s in subjects_list):
        raise ValueError("Subjects list should contain strings only.")
    return [s.strip() for s in subjects_list if s.strip()]
