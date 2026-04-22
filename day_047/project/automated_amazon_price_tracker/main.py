import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
SENDER = os.getenv("SENDER_EMAIL")
RECEIVER = os.getenv("RECEIVER_EMAIL")
PASSWORD = os.getenv("GOOGLE_SMTP_PASSWORD")

response = requests.get(url=url, headers={"User-Agent": "CCBot/2.0 (https://commoncrawl.org/faq/)"})
soup = BeautifulSoup(response.content, "html.parser")

price_whole = soup.find("span", {"class": "a-price-whole"})
price_fraction = soup.find("span", {"class": "a-price-fraction"})
product_item = soup.find("h1", {"id": "title"}).text.strip()
price = float(price_whole.text + price_fraction.text)

message = f"Hot offer!\nProduct: {product_item} \nPrice: {price} \nBuy here: https://appbrewery.github.io/instant_pot/ \nThis is an automated email. Do not answer."

if price < 100:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=SENDER, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER,
            to_addrs=RECEIVER,
            msg=message.encode("utf-8"),
        )
        print("Email sent!")
