# List exercises

# Create new list with num+1 from number
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = [n+1 for n in numbers]

# Create new letter list
name = "Ruslan"
letter_list = [letter for letter in name]

# Create new doubled range list
range_list = [num*2 for num in range(10) ]

# Conditional lists

# Take all short names <= 5 characters in ALL CAPS
names = ["Ruslan", "Emily","Caroline","McDonald","Kevin"]
short_names = [name.upper() for name in names if len(name)<=5]
print(short_names)


