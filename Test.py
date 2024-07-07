import streamlit as st
from firebase_admin import firestore
import json
from google.oauth2.service_account import Credentials

key_dict = json.loads(st.secrets["textkey"])
creds = Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds)

doc_ref = db.collection("Token")
doc = doc_ref.get()

token_list = [i.to_dict()['device'] for i in doc]
print(token_list)