from datetime import datetime, timedelta

def generate_study_plan(total_hours, subjects, exams, weak_subjects, strong_subjects):
    today = datetime.today()
    days_until_exams = {}
    for subject, exam_date in exams.items():
        days_left = max((exam_date - today).days, 1)
        days_until_exams[subject] = days_left

    base_hours_per_day = total_hours / len(subjects)
    plan = {}

    for subject in subjects:
        priority = 1
        if subject in weak_subjects:
            priority += 1.5
        if subject in strong_subjects:
            priority -= 0.5
        time_factor = 1 / days_until_exams.get(subject, 10)
        hours = base_hours_per_day * priority * (1 + time_factor)
        plan[subject] = round(hours, 2)

    total_allocated = sum(plan.values())
    for subject in plan:
        plan[subject] = round(plan[subject] * total_hours / total_allocated, 2)

    return plan

# Example call
if __name__ == "__main__":
    total_hours = 6
    subjects = ["Math", "Physics", "Chemistry", "English"]
    exams = {
        "Math": datetime.strptime("2025-10-10", "%Y-%m-%d"),
        "Physics": datetime.strptime("2025-10-12", "%Y-%m-%d"),
        "Chemistry": datetime.strptime("2025-10-20", "%Y-%m-%d"),
        "English": datetime.strptime("2025-10-25", "%Y-%m-%d"),
    }
    weak_subjects = ["Math", "English"]
    strong_subjects = ["Physics"]

    schedule = generate_study_plan(total_hours, subjects, exams, weak_subjects, strong_subjects)
    print("Daily Study Plan (hours):")
    for subj, hrs in schedule.items():
        print(f"{subj}: {hrs}")
