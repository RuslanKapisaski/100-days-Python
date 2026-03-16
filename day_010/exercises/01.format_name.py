#Create a function called format_name() that takes two inputs: f_name and l_name.

def format_name(f_name,l_name):
    return  f"{f_name.title()} {l_name.title()}"


name = format_name("ruslan","kapisaski")
print(name)