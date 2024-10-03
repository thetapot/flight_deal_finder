from os import getenv

from dotenv import load_dotenv
from twilio.rest import Client
import os

# Load environment variables from .env file
load_dotenv()

class NotificationManager:
    def __init__(self):
        self.client = Client(getenv('ACCOUNT_SID'), getenv('AUTH_TOKEN'))

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=getenv('TWILIO_WHATSAPP_NUMBER'),
            body=message_body,
            to=getenv('TWILIO_VERIFIED_NUMBER')
        )

        print(message.sid)
