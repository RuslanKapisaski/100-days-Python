import random

names =["Alice", "Bob", "Charlie", "David","Marry","Derry"]
students_scores = {student:random.randint(1, 100) for student in names}
print(f"Results: {students_scores}")
passed_students = {student:score for (student, score) in students_scores.items() if score > 50}
print(f"Passed: {passed_students}")
