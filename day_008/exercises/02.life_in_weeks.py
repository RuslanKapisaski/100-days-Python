# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.


def life_in_weeks(age):
    total_ages = 90
    total_weeks = total_ages * 52
    current_weeks = age * 52
    left_weeks = total_weeks - current_weeks
    return print("You have", left_weeks, "weeks left.")


life_in_weeks(56)