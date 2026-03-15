# Grading Program
# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and the values are their exam scores.

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    grade = student_scores[key]
    if 91 <= grade <= 100:
        grade = "Outstanding"
    elif 81 <= grade <= 90:
        grade = "Exceeds Expectations"
    elif 71 <= grade <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[key] = grade

for key in student_grades:
    print(student_grades[key])
