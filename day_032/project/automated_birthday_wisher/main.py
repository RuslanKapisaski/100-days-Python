import smtplib
import datetime as dt
from random import choice
import pandas as pd

def send_gmail(name, email, letter):
    my_email = "rkapisaski@gmail.com"
    password = "yourpassword"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    message = f"Subject: Happy Birthday!\n\n{letter}"
    connection.sendmail(
        from_addr=my_email,
        to_addrs=email,
        msg=message,
    )

def get_date():
    today = dt.date.today()
    return today.month, today.day

def fetch_csv_data():
    data = pd.read_csv("birthdays.csv")
    return data

with open("./letter_templates/letter_2.txt", "r") as file:
    letter_template = file.read()

birthday_data = fetch_csv_data()
today_month, today_day = get_date()

for _, row in birthday_data.iterrows():
    if row["month"] == today_month and row["day"] == today_day:
        letter = letter_template.replace("[NAME]", row["name"])
        send_gmail(row["name"], row["email"], letter)