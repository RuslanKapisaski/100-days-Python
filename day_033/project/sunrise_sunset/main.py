import requests
import smtplib
import datetime

MY_LAT = 42.672914
MY_LONG = 23.327414
MY_EMAIL = "rkapisaski@gmail.com"
MY_PASSWORD = "yourpassword"

SUNRISE_SUNSET_PARAMS = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])


    lat_close = MY_LAT - 5 < iss_lat < MY_LAT + 5
    long_close = MY_LONG - 5 < iss_long < MY_LONG + 5

    return lat_close and long_close


def is_dark():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=SUNRISE_SUNSET_PARAMS)
    response.raise_for_status()
    data = response.json()

    # "2024-01-01T06:30:00+00:00"
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    current_hour = datetime.datetime.now().hour

    return current_hour >= sunset or current_hour <= sunrise


def send_email(receiver_email):

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Encrypt the connection
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=receiver_email,
            msg="Subject: ISS Alert!\n\nLook up! The ISS is above you!"
        )

overhead = is_overhead()
dark = is_dark()

if overhead and dark:
    send_email(MY_EMAIL)
    print("Email sent!")
else:
    print(f"ISS overhead: {overhead}, Dark outside: {dark}")