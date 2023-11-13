'''
Services related to Twilio SMS sender
'''
import os
from dotenv import load_dotenv
from twilio.rest import Client
from fastapi import status
from fastapi.exceptions import HTTPException

load_dotenv()

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")

class Twilio:
    '''
    Class to handle Twilio related methods
    '''
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)
    async def send_message(self, client_phone, message_body):
        '''
        Sends SMSs 
        '''
        message = self.client.messages \
            .create(
                body=message_body,
                from_=PHONE_NUMBER,
                to=client_phone
            )

        if not message.status == 'sent':
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error sending twilio SMS"
            )
