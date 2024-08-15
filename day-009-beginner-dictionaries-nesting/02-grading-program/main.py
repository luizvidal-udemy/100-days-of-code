student_scores = {"Harry": 88, "Ron": 78, "Hermione": 95, "Draco": 75, "Neville": 60}

student_grades = {}

# - Scores 91 - 100: Grade = "Outstanding"

# - Scores 81 - 90: Grade = "Exceeds Expectations"

# - Scores 71 - 80: Grade = "Acceptable"

# - Scores 70 or lower: Grade = "Fail"


def get_student_grade(score: int) -> str:
    if score <= 70:
        return "Fail"
    elif score <= 80:
        return "Acceptable"
    elif score <= 90:
        return "Exceeds Expectations"
    else:
        return "Outstanding"

for key in student_scores:
    student_grades[key] = get_student_grade(student_scores[key])


print(student_grades)