import streamlit as st
from utils import map, chatbot
from firebase_admin import firestore
import json
from google.oauth2.service_account import Credentials

key_dict = json.loads(st.secrets["textkey"])
creds = Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds)

# anamnesis is medical history 

css = '''
<style>
    [data-testid='stImage'] {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        overflow: hidden;
    }
     }

    [data-testid='stExpander'] {
        border: none;
        box-shadow: none;

    }
    [data-testid='stExpander'] section {
        overflow: hidden;
        text-align: center;
        display: inline-block;
        width: 100%;
        margin-right: -50%;

    }
    [data-testid='stExpander'] section + div {
        float: right;
    }
    }
    [class='folium-map leaflet-container leaflet-touch leaflet-retina leaflet-fade-anim leaflet-grab leaflet-touch-drag leaflet-touch-zoom'] section
        height: 200px;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)
def load_stored_image():
    doc_ref = db.collection("Users").document(id['uid'])

    # Get the image data (Base64 string)
    doc = doc_ref.get()
    image_data = doc.to_dict().get('Image')

    if image_data is None:
        return None
    
    return st.image(image_data, width=200, use_column_width ='auto')

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
    st.markdown(f"**{name}**")
    st.markdown(f"Tuổi: {age} <br>SDT: {phone}<br>Tiền sử: {anamnesis}",unsafe_allow_html=True)


def main():
    #st.write(id)
    display_profile()

if __name__ == "__main__":
    st.title("HI card📋")
    id = st.query_params.to_dict()
    col1, col2 = st.columns([3, 5])

    #with col1:
    load_stored_image()
    main()
    st.divider()
        #with st.expander(":toolbox: Hỏi HI-assistant"):
            #chatbot.sidebar_chatbot()
    #with col2:
        #with st.container(border= True):
            #map.pinpoint()
