# For-loops
# Highest Score
# Description
# Python has lots of built-in functions to help us work with numbers.
# One of them helps us calculate the sum (the total). e.g.
# student_scores = [180, 124, 165, 173, 189, 169, 146]
# 1 Replicate sum
# 2 Replicate max

#1. Sum custom decision
student_scores = [180, 124, 165, 173, 189, 169, 146]
total = 0
for score in  student_scores:
    total += score
print(f"Total: {total}")

#1.1 Using built-in function sum`
total_sum = sum(student_scores)
print(f"Total sum: {total_sum}")


#2 Max custom decision
max_score = student_scores[0]
for score in student_scores:
    if(max_score) < score:
        max_score = score
print(f"\nMax score: {max_score}")

#2 Using built-in function max
max = max(student_scores)
print(f"Max: {max}")