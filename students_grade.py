student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[student] = grade
    
print(student_grades)