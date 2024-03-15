import streamlit as st
from utils import function, chatbot
from firebase_admin import firestore
import json
from google.oauth2.service_account import Credentials

key_dict = json.loads(st.secrets["textkey"])
creds = Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds)


#db = firestore.Client.from_service_account_json("key.json", project="CARD")
def load_user():
    doc_ref = db.collection("Users").document(id['uid'])
    doc = doc_ref.get()
    dic = doc.to_dict()
    if dic is not None:
        age = dic.get('Age')
        name = dic.get('Name')
        phone = dic.get('Phone')
        anamnesis = dic.get('Anamnesis')
        return age,name,phone,anamnesis
    else:
        return None,None,None,None


def display_profile():
    age,name,phone,anamnesis = load_user()
    name = st.info('Name: '+name)
    age = st.info('Age: '+age)
    phone = st.info('Phone: '+phone)
    anamnesis = st.info('Anamnesis: '+anamnesis)


def main():
    #st.write(id)
    display_profile()

if __name__ == "__main__":
    st.title("HI card - patient information 📋")
    id = st.query_params.to_dict()
    if id.keys() is not None:
        chatbot.sidebar_chatbot()
        main()
