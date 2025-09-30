import streamlit as st
import joblib
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from modules.utils import clean_text, parse_exam_dates, validate_subjects

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from modules.study_plan import generate_study_plan

models_dir = os.path.join(project_root, "models")

clf = joblib.load(os.path.join(models_dir, "expense_classifier_emb.pkl"))
embedder = joblib.load(os.path.join(models_dir, "embedder.pkl"))

st.set_page_config(page_title="Expense & Study Planner", layout="centered")

st.title("Expense Categorizer & Study Plan Generator")

tab1, tab2 = st.tabs(["Expense Categorizer", "Study Plan Generator"])

if "expenses" not in st.session_state:
    st.session_state.expenses = []

def add_expense(text, category):
    st.session_state.expenses.append({"text": text, "category": category})

with tab1:
    st.header("Expense Categorizer")
    user_input = st.text_input("Enter transaction text:")
    if st.button("Categorize"):
        if user_input.strip():
            processed = clean_text(user_input)
            emb = embedder.encode([processed])
            category = clf.predict(emb)[0]
            add_expense(user_input, category)
            st.success(f"Predicted Category: {category}")

            df_expenses = pd.DataFrame(st.session_state.expenses)
            if not df_expenses.empty:
                counts = df_expenses['category'].value_counts()

                st.write("### Expense Category Distribution")
                st.bar_chart(counts)

                fig, ax = plt.subplots()
                counts.plot.pie(autopct='%1.1f%%', ax=ax)
                ax.set_ylabel("")
                st.pyplot(fig)
        else:
            st.warning("Please enter transaction text.")

with tab2:
    st.header("Study Plan Generator")
    total_hours = st.number_input("Total available study hours per day", min_value=1, max_value=24, value=6)
    subjects_text = st.text_area("Subjects (comma separated)", "Math, Physics, Chemistry, English")
    upcoming_exams_text = st.text_area("Upcoming exams (subject:YYYY-MM-DD, one per line)",
                                       "Math:2025-10-10\nPhysics:2025-10-12\nChemistry:2025-10-20\nEnglish:2025-10-25")
    weak_subjects_text = st.text_input("Weak subjects (comma separated)", "Math, English")
    strong_subjects_text = st.text_input("Strong subjects (comma separated)", "Physics")

    if st.button("Generate Study Plan"):
        try:
            subjects = validate_subjects(subjects_text.split(","))
            exams = parse_exam_dates(upcoming_exams_text)
            weak_subjects = validate_subjects(weak_subjects_text.split(","))
            strong_subjects = validate_subjects(strong_subjects_text.split(","))
            plan = generate_study_plan(total_hours, subjects, exams, weak_subjects, strong_subjects)
            st.subheader("Daily Study Plan (Hours)")
            for subj, hours in plan.items():
                st.write(f"{subj}: {hours}")
        except Exception as e:
            st.error(f"Error: {e}")
