# Positional vs Keyword Arguments

# Description
# Multiple Inputs
# You can have multiple inputs in functions. All you need to do is separate them with a comma


def greet_with(name, location):
    print(f"Welcome, {name}")
    print(f"Have a nice trip in {location}")

#Positional argument - we have to be aware of not changing arguments order
greet_with("Peter","Bansko")

#Keyword argument
greet_with(location="Basnko",name="Peter")