# Data Overlap
# 💪 This exercise is HARD 💪
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
# e.g. if file1.txt contained:
# 1
# 2
# 3
# and file2.txt contained:
# 2
# 3
# 4
# result = [2, 3]

with open("file1.txt") as f1, open("file2.txt") as f2:
    f1_content = f1.readlines()
    f2_content = f2.readlines()

    f1_numbers = [int(n.strip()) for n in f1_content]
    f2_numbers = [int(n.strip()) for n in f2_content]

result = [n for n in f1_numbers if n in f2_numbers]
print(result)
