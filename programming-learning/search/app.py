import streamlit as st
import requests

# 🔑 Apna API key yaha daalo
API_KEY = "YOUR_GOOGLE_API_KEY"
CX = "YOUR_SEARCH_ENGINE_ID"

# Google Search Function
def google_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY,
        "cx": CX,
        "q": query
    }
    response = requests.get(url, params=params)
    return response.json()

# Response filter function
def get_filtered_answer(data):
    if "items" not in data:
        return "Koi result nahi mila"

    results = data["items"][:3]
    answer = ""

    for item in results:
        title = item["title"]
        snippet = item["snippet"]
        link = item["link"]

        answer += f"🔹 {title}\n{snippet}\n{link}\n\n"

    return answer

# Streamlit UI
st.title("🔍 AI Google Search Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Kuch bhi search karo...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)

    # Google search
    data = google_search(user_input)
    response = get_filtered_answer(data)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)