from tkinter import *
from tkinter import messagebox
import string
import random
import json
import os
import sys

# ---------------------------- SETUP DMG FILE ------------------------------- #

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password = ''
    for i in range(18):
        password += random.choice(string.ascii_letters)
    password_entry.insert(0, password)

# ---------------------------- LOAD DATA ------------------------------- #
def load_data(user_input):
    reset()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        website_entry.insert(0, "No data found")
    else:
        if user_input.lower() in data:
            email = data[user_input.lower()]['Email: ']
            password = data[user_input.lower()]['Password: ']
            username_email_entry.insert(0, email)
            password_entry.insert(0, password)
        else:
            messagebox.showinfo("Oops", "Not found")
    finally:
        add_btn.config(state="disabled")
        load_btn.config(state="disabled")
        generate_pass_btn.config(state="disabled")

# ---------------------------- WEBSITE CHANGE ------------------------------- #
def on_website_change(*args):
    if website_entry.get().strip():
        add_btn.config(state="normal")
        load_btn.config(state="normal")
        generate_pass_btn.config(state="normal")
    else:
        add_btn.config(state="disabled")
        load_btn.config(state="disabled")
        generate_pass_btn.config(state="disabled")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def reset():
    website_entry.delete(0, END)
    username_email_entry.delete(0, END)
    password_entry.delete(0, END)

def save_data(website, username_or_email, password):
    new_data = {
        website.lower(): {
            "Email: ": username_or_email,
            "Password: ": password,
        }
    }
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    reset()

def are_empty_fields(website, username_email, password):
    is_empty = False
    message_label = Label(text="")
    message_label.grid(column=1, row=5, sticky="ew")
    message_label.config(fg="red")

    if website == "":
        message_label.config(text="Website is required.")
        is_empty = True
    elif username_email == "":
        message_label.config(text="Username is required.")
        is_empty = True
    elif password == "":
        message_label.config(text="Password is required.")
        is_empty = True
    return is_empty

def get_text():
    website = website_entry.get()
    username_email = username_email_entry.get()
    password = password_entry.get()

    if not are_empty_fields(website, username_email, password):
        save_data(website, username_email, password)

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.configure(padx=100, pady=50)

img = PhotoImage(file=resource_path("logo.png"))

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=img)

website_label = Label(text="Website")
username_email_label = Label(text="Email/Username")
password_label = Label(text="Password")

website_entry = Entry(width=30)
website_entry.focus()
website_var = StringVar()
website_entry.config(textvariable=website_var)
website_var.trace("w", on_website_change)

username_email_entry = Entry(width=35)
password_entry = Entry(width=30)

generate_pass_btn = Button(text="Generate Pass", width=10, state="disabled", command=generate_pass)
add_btn = Button(text="Add", width=32, state="disabled", command=get_text)
load_btn = Button(text="Load", width=10, state="disabled", command=lambda: load_data(website_entry.get()))

# Positioning
canvas.grid(row=0, column=1)

website_label.grid(row=1, column=0, sticky="e")
username_email_label.grid(row=2, column=0, sticky="e")
password_label.grid(row=3, column=0, sticky="e")

website_entry.grid(row=1, column=1, sticky="w")
username_email_entry.grid(row=2, column=1, sticky="w")
password_entry.grid(row=3, column=1, sticky="w")

generate_pass_btn.grid(row=3, column=1, sticky="e")
add_btn.grid(row=4, column=1, columnspan=2)
load_btn.grid(row=1, column=1, sticky="e")

screen.mainloop()