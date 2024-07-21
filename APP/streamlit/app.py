import streamlit as st
import requests
import json
def get_bot_response(user_input):
    url = "http://rasa-server:5005/webhooks/rest/webhook"
    payload = {"sender": "user", "message": user_input}
    response = requests.post(url, json=payload)
    response = json.dumps(response.json())
    response = json.loads(response)
    bot_response = ""
    print(response)
    for res in response:
        print(res)
        for key, value in res.items():
            if key == 'recipient_id':
                pass
            if key == 'image':
                #bot_response = bot_response + "https://i.imgur.com/0jD8Y7H.png" + "  \n"
                #st.chat_message("AI").write(st.image("https://i.imgur.com/0jD8Y7H.png"))
                st.chat_message("AI").image(value)
                st.session_state.messages.append({"role": "AI", "image": value})
            if key == 'text':
                #bot_response = bot_response + value + "  \n"
                st.chat_message("AI").write(value)
                st.session_state.messages.append({"role": "AI", "message": value})
            if key == 'attachment':
                # bot_response = bot_response + value + "  \n"
                values = value['payload']['src']
                st.chat_message("AI").video(values)
                st.session_state.messages.append({"role": "AI", "video": values})
    #return bot_response

def CreateApp():
    #print('hey!!')
    st.title("Welcome to Simple Rasa ChatBot With Streamlit")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "AI", "message": "How can I help you?"}]


    for msg in st.session_state.messages:
        #print(msg)
        #st.chat_message(msg["role"]).write(msg["message"])
        #Source - https://discuss.streamlit.io/t/chatbot-app-with-images-in-chat/61162
        for key, value in msg.items():
            if key == 'role':
                pass
            if key == 'image':
                with st.chat_message(msg["role"]):
                    st.image(value)
            if key == 'video':
                with st.chat_message(msg["role"]):
                    st.video(value)
            if key == 'message':
                with st.chat_message(msg["role"]):
                    st.write(value)

    user_input = st.chat_input()

    if user_input:
        st.chat_message("User").write(user_input)
        st.session_state.messages.append({"role": "User", "message": user_input})
        get_bot_response(user_input)
        #response = get_bot_response(user_input)
        # st.chat_message("AI").write(response)
        #st.text_area("Bot Response", value=response, height=200, max_chars=None, key=None)
        #st.session_state.messages.append({"role": "AI", "message": response})


if __name__ == "__main__":
    CreateApp()


