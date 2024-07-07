import streamlit as st
from utils import map, chatbot, FCMManager
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
    # Get the image data (Base64 string)
    doc_ref = db.collection("Users").document(id['uid'])
    doc = doc_ref.get()
    image_data = doc.to_dict().get('Image')
    if image_data is None:
        return None
    return st.image(image_data, width=200, use_column_width ='auto')

def load_user():
    doc_ref = db.collection("Users").document(id['uid'])
    doc = doc_ref.get()
    dic = doc.to_dict()
    if dic is not None:
        return dic 

def display_profile():
    dic = load_user()
    st.markdown(f"**{dic['Name']}**")
    st.markdown(f"Tuổi: {dic['Age']} <br>SDT: {dic['Phone']}<br>Tiền sử: {dic['Anamnesis']}",unsafe_allow_html=True)

def main():
    #st.write(id)
    display_profile()

if __name__ == "__main__":
    st.title("HI card📋")
    id = st.query_params.to_dict()
    col1, col2 = st.columns([3, 5])
    dic = load_user()
    with col1:
        if st.button("Gọi Cứu Thương!!!"):
            doc_ref = db.collection("Token")
            doc = doc_ref.get()
            token_list = [i.to_dict()['device'] for i in doc]
            #token = ['cL-KKticS8CLY9qLxpwWtw:APA91bEPLVmuQ1rOIQfTGXXOnZl5oAlS0MV9D-jbivEG9G0dq4v0PaR0lpE-O_Icvi2eTCXxJV9yYTX2swahYQK_Bjv98kE0wzUNjWnad1U-RHjknaDJcwbTZNdvc62XAopf6CL_zOXh']
            FCMManager.sendPush("Hi-Card", "HAHAH GHÊ CHƯA- Tín đẹp trai!!!", token_list)
        load_stored_image()
    with col2:
        main()
    st.divider()
    with st.expander(":toolbox: Hỏi HI-assistant"):
        chatbot.sidebar_chatbot()
    with col2:
        with st.container(border= True):
            map.pinpoint()
