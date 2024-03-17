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
    st.set_page_config(page_title="HI-card", layout="centered", initial_sidebar_state="auto", menu_items=None)
    st.title("HI card - patient information 📋")
    id = st.query_params.to_dict()
    col1, col2 = st.columns([4, 2])
    if id.keys() is not None:
        #with col1:
        main()
        #with col2:
        chatbot.sidebar_chatbot()
        
