import streamlit as st
import time

st.title("🏗️ Layouts & System")

tab1, tab2 = st.tabs(["Alerts", "Containers"])

with tab1:
    st.success("This is a success message!")
    st.info("Here is some info.")
    st.warning("Be careful!")
    st.error("Something went wrong.")

with tab2:
    with st.expander("Click to expand details"):
        st.write("Streamlit makes UI design very easy using containers.")

st.divider()
if st.button("Run Simulation"):
    with st.spinner("Processing..."):
        time.sleep(2)
    st.balloons()
    st.toast("Done!", icon="✅")