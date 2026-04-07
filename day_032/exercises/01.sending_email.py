import smtplib

my_email = "rkapisaski@gmail.com"
password = "yourpassword"

server = smtplib.SMTP("smtp.gmail.com", 587)

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="manovae90@gmail.com",
    msg=f"Hello!",
)
