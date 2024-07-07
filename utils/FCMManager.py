import firebase_admin
from firebase_admin import credentials, messaging
from firebase_admin import firestore
from google.oauth2.service_account import Credentials
import json
import streamlit as st

key_dict = json.loads(st.secrets["textkey"])
creds = credentials.Certificate(key_dict)
try:
    firebase_admin.get_app()
except ValueError:
    firebase_admin.initialize_app(creds)

def sendPush(title, msg, registration_token, dataObject=None):
    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg
        ),
        data=dataObject,
        tokens=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send_multicast(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)