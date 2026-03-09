# Check Odd or Even
# Write some code using what you have learnt about the modulo operator and conditional checks in Python to check if the number in the input area is odd or even.
# If it's odd print out the word "Odd" otherwise printout "Even".

number = int(input("Type a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")