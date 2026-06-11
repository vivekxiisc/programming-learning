import streamlit as st

st.title("🖱️ Basic Widgets & Inputs")

col1, col2 = st.columns(2)
with col1:
    st.header("Text & Numbers")
    st.text_input("Enter name", "User")
    st.number_input("Select Age", 0, 100, 25)
    st.text_area("Your Bio")
    
with col2:
    st.header("Selection")
    st.selectbox("Pick one", ["A", "B", "C"])
    st.multiselect("Pick many", ["Red", "Blue", "Green"])
    st.slider("Level", 0, 100, 50)

st.divider()
st.file_uploader("Upload Data")
st.color_picker("Choose a theme color")