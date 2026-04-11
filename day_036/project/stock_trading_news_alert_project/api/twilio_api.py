import os
from dotenv import load_dotenv
import time

from twilio.rest import Client

load_dotenv()

# Twilio SMS
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
def determine_emoji(change_percentage):
    if change_percentage > 0:
        return  '🔺'
    else:
        return  '🔻'

def send_sms(data):
    client = Client(account_sid, auth_token)
    emoji = determine_emoji(data['change'])

    formatted_message = (f"TSLA: {emoji}\nHeadline: {data['article_data']['title']}\n"
                         f"Brief: {data['article_data']['description']}\n"
                         f"Author: {data['article_data']['author']}\n")

    message = client.messages.create(
        to="+359884847216",
        from_="+15754002212",
        body=formatted_message)

    time.sleep(5)

    # fetch updated status
    updated = client.messages(message.sid).fetch()
    print(updated.status)  # delivered / failed / undelivered
    print(updated.error_code)  # None if ok, error code if failed
    print(updated.error_message)



