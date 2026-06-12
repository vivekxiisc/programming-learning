import streamlit as st

# Setup the navigation structure
pg = st.navigation([
    st.Page("page_1.py", title="Inputs & Widgets", icon="🖱️"),
    st.Page("page_2.py", title="Data & Charts", icon="📊"),
    st.Page("page_3.py", title="Layouts & Status", icon="🏗️"),
    st.Page("page_4.py", title="AI & Chat", icon="🤖"),
])

# Global Page Config (applies to all pages)
st.set_page_config(page_title="Streamlit Master", layout="wide")

# Run the navigation
pg.run()