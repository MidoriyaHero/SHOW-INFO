import google.generativeai as genai
import streamlit as st
import json
key_dict = json.loads(st.secrets["geminikey"])
api = key_dict['api']
def generate_response(prompt_input):

    genai.configure(api_key=api)
    model = genai.GenerativeModel('gemini-pro')                      
    chatbot = model.generate_content(prompt_input)
    return chatbot.text
def sidebar_chatbot():
    #ith st.sidebar():
        st.title('HI bot')
        # Store LLM generated responses
        if "messages" not in st.session_state.keys():
            st.session_state.messages = [{"role": "assistant", "content": "Tôi có thể giúp gì cho bạn?"}]

        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])


        # User-provided prompt
        if prompt := st.chat_input("Bạn đang có chuyện gấp sao?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

        # Generate a new response if last message is not from assistant
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = generate_response(f'Giả sử bạn là 1 bác sĩ giỏi với nhiều năm kinh nghiệm,từ giờ hãy trả lời tôi MỘT CÁCH NGẮN GỌN và nhanh chóng:{prompt}') 
                    st.write(response) 
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message)



        reset_button_key = "reset_button"
        reset_button = st.button("Reset Chat",key=reset_button_key)
        if reset_button:
            st.session_state.messages = []

if __name__ == "__main__":
    sidebar_chatbot()
        