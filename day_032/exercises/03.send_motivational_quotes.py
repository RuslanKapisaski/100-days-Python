import smtplib
import datetime as dt
from random import choice

def send_gmail(quote,date):
    my_email = "rkapisaski@gmail.com"
    password = "yourpassword"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    message = f"Subject: Quote of the Day\n\nQuote of the {date}:\n{quote}"
    print(message)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="manovae90@gmail.com",
        msg=message,
    )

def get_date():
    today = dt.date.today()
    return today

with open("./quotes.txt","r") as file:
    quotes = file.readlines()
    random_quote = choice(quotes)
    date = get_date()
    send_gmail(random_quote,date)



