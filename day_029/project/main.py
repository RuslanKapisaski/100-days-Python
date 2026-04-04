import string
import webbrowser
from tkinter import *
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password = ''
    for i in range(18):
        password += random.choice(string.ascii_letters)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def reset():
    website_entry.delete(0, END)
    username_email_entry.delete(0, END)
    password_entry.delete(0, END)
    
def save_data(website,username_or_email,password):
    with open("data.txt", "a") as file:
        file.write(f"{website} | {username_or_email} | {password}\n")
    reset()

def are_empty_fields(website,username_email,password):
    is_empty = False
    message_label = Label(text="")
    message_label.grid(column=1, row=5, sticky="ew")
    message_label.config(fg="red")

    if (website == ""):
        message_label.config(text="Website is required.")
        is_empty = True
    elif(username_email == ""):
        message_label.config(text="Username is required.")
        is_empty = True
    elif(password == ""):
        message_label.config(text="Password is required.")
        is_empty = True
    return is_empty

def get_text():
    website = website_entry.get()
    username_email = username_email_entry.get()
    password = password_entry.get()

    if not are_empty_fields(website,username_email,password):
        save_data(website, username_email, password)

# ---------------------------- UI SETUP ------------------------------- #
# Create UI
screen = Tk()
screen.title("Password Manager")
screen.configure(padx=100,pady=50)

img = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200)
canvas.create_image(100,100,image=img)

website_label = Label(text="Website")
username_email_label = Label(text="Email/Username")
password_label = Label(text="Password")

website_entry = Entry(width=35)
website_entry.focus()
username_email_entry = Entry(width=35)
password_entry = Entry(width=21)

generate_pass_btn = Button(text="Generate Password",width=21,command=generate_pass)
add_btn = Button(text="Add",width=36, command=get_text)

# Positioning
canvas.grid(row=0,column=1)

website_label.grid(row=1, column=0, sticky="e")
username_email_label.grid(row=2, column=0, sticky="e")
password_label.grid(row=3, column=0, sticky="e")

website_entry.grid(row=1,column=1)
username_email_entry.grid(row=2,column=1)
password_entry.grid(row=3,column=1,sticky="w")

generate_pass_btn.grid(row=3,column=1,sticky="e")
add_btn.grid(row=4,column=1,columnspan=2)

screen.mainloop()