


import streamlit as st 
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import time


@st.cache_resource
def get_client():
    load_dotenv()
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except:
        api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        st.error("❌ GEMINI_API_KEY not found. Add it in Streamlit Cloud secrets.")
        st.stop()
    
    return genai.Client(api_key=api_key)



client = get_client()

st.title("Ai chatbot")
st.caption("Gemini")

# sidebar
persona = st.sidebar.selectbox(
    "Ai personality:",
    ["Helpful assistant", "Sarcastic", "Roasting", "Tutor"]
)


personas = {
    "Helpful assistant": "you are a helpful, friendly Ai assistant. Be concise.",
    "Sarcastic": "you are sarcastic. answer with sarcasm",
    "Roasting": "Roast the user brutally",
    "Tutor": "You are a tutor, explain clearly"
}


# chat session
if "chat" not in st.session_state or st.session_state.get("persona") != persona:
    st.session_state.chat = client.chats.create(
        model="gemini-3.6-flash",
        config=types.GenerateContentConfig(
            system_instruction=personas[persona]
        )
    )
    st.session_state.messages = []
    st.session_state.persona = persona

# chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# input 
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role":"user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full = ""
        for chunk in st.session_state.chat.send_message_stream(prompt):
            for char in chunk.text:
                full += char
                placeholder.markdown(full + "| ")
                time.sleep(0.005)
        placeholder.markdown(full)

    st.session_state.messages.append({"role":"assistant", "content":full})