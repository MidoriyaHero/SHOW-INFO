import google.generativeai as genai
import streamlit as st
import json
from firebase_admin import firestore
from google.oauth2.service_account import Credentials

key_dict = json.loads(st.secrets["textkey"])
creds = Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds)

key_dict = json.loads(st.secrets["geminikey"])
api = key_dict['api']

def generate_response(prompt_input):
    genai.configure(api_key=api)
    model = genai.GenerativeModel('gemini-pro')
    chatbot = model.generate_content(prompt_input)
    # Access the text content correctly based on the response structure
    if chatbot.candidates:
        if len(chatbot.parts) == 1:
            text = chatbot.text
            text = ""
            for part in chatbot.parts:
                text += part.text + "\n"
        elif len(chatbot.parts) >=1:
            text = ""
            for part in chatbot.parts:
                text += part.text + "\n" 
        else:
            text = ' '
    else:
        text =' '
    return text

def sidebar_chatbot():
        id = st.query_params.to_dict()
        doc_ref = db.collection("Users").document(id['uid'])
        doc = doc_ref.get()
        tien_su = doc.to_dict().get('Anamnesis')
        if "messages" not in st.session_state.keys():
            st.session_state.messages = [{"role": "assistant", "content": "Tôi có thể giúp gì cho bạn?"}]

        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
        # User-provided prompt
        if prompt := st.chat_input("Hỏi nhanh:"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)
        # make quick question
          
        if st.button(f'Dấu hiệu người bị {tien_su}',key = 'tindeptrai'):
            with st.chat_message("user"):
                prompt = (f'Dấu hiệu người bị {tien_su}')
                st.write(prompt)
                st.session_state.messages.append({"role": "user", "content": prompt})
        if st.button(f'Sơ cứu người bị {tien_su}',key = 'tin'):
            with st.chat_message("user"):
                prompt = (f'Cấp cứu người bị {tien_su}')
                st.write(prompt)
                st.session_state.messages.append({"role": "user", "content": prompt})
        # Generate a new response if last message is not from assistant
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Chờ chút nhé~"):
                    response = generate_response(f'Giả sử bạn là 1 bác sĩ giỏi với nhiều năm kinh nghiệm/n,\
                                                 từ giờ hãy trả lời tôi MỘT CÁCH NGẮN GỌN, nhanh chóng, \
                                                 đơn giản và không đề nghị sử dụng bất kì loại thuốc gì vì đây là vấn đề liên quan đến mạng sống con người\
                                                    :{prompt}') 
                    st.write(response) 
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message)

if __name__ == "__main__":
    sidebar_chatbot()
        