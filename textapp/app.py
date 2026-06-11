import streamlit as st
from datetime import datetime

# 1. Page Configuration (Browser tab aur icon)
st.set_page_config(page_title="V-Chat Private", page_icon="💬", layout="centered")

# 2. Styling (WhatsApp jaisa look dene ke liye)
st.markdown("""
    <style>
    .stChatMessage { border-radius: 15px; padding: 10px; margin: 5px 0; }
    .st-emotion-cache-1c79332 { background-color: #dcf8c6; } /* Sent message color */
    </style>
    """, unsafe_allow_html=True)

# 3. Session State Initialization (Chat memory setup)
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# 4. Sidebar (Login aur Room selection)
with st.sidebar:
    st.title("🔐 V-Chat Access")
    if not st.session_state.user_name:
        name = st.text_input("Apna Naam daalein:", placeholder="e.g. Vivek")
        if st.button("Join Chat"):
            if name:
                st.session_state.user_name = name
                st.rerun()
    else:
        st.success(f"Logged in as: **{st.session_state.user_name}**")
        st.write("Room: **Global Room**")
        if st.button("Logout"):
            st.session_state.user_name = ""
            st.session_state.messages = []
            st.rerun()

# 5. Main Chat Interface
st.title("💬 V-Chat Messenger")

# Purane messages display karna
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(f"**{message['user']}**")
        st.write(message["content"])
        st.caption(message["time"])

# 6. Chat Input (Naya message bhejne ke liye)
if st.session_state.user_name:
    if prompt := st.chat_input("Type a message..."):
        # Time nikalna
        current_time = datetime.now().strftime("%I:%M %p")
        
        # Message ko memory mein save karna
        new_msg = {
            "role": "user", 
            "user": st.session_state.user_name, 
            "content": prompt, 
            "time": current_time
        }
        st.session_state.messages.append(new_msg)
        
        # UI refresh karke naya message dikhana
        st.rerun()
else:
    st.info("👈 Please enter your name in the sidebar to start chatting.")

# 7. System Logic (Agar message list khali hai toh welcome message)
if not st.session_state.messages and st.session_state.user_name:
    st.write("System: *Koi messages nahi hain. Pehla message bhejein!*")