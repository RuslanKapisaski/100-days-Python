import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

twilio_account_sid = os.getenv("TWILIO_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_virtual_number = os.getenv("TWILIO_VIRTUAL_NUMBER")
twilio_verified_number = os.getenv("TWILIO_VERIFIED_NUMBER")
print(twilio_account_sid, twilio_virtual_number, twilio_verified_number)
class NotificationManager:
    def __init__(self):
        self.price = 0
        self.departure_airport = ""
        self.iata_code = ""
        self.in_date = ""
        self.out_date = ""

    def send_sms(self, message_body):
        client = Client(twilio_account_sid, twilio_auth_token)
        print(len(message_body))
        message = client.messages.create(
            to=twilio_verified_number,
            from_=twilio_virtual_number,
            body=message_body
        )

        # Check the status of sent message
        updated = client.messages(message.sid).fetch()
        print(f"Status: {updated.status}")
        if updated.status == "failed":
            print(f"Error code: {updated.error_code}")
            print(f"Error message: {updated.error_message}")