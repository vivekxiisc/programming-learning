import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Data & Visualization")

# Generate random data
data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])

st.subheader("Interactive Metrics")
m1, m2 = st.columns(2)
m1.metric("Revenue", "$50,000", "+10%")
m2.metric("Loss", "$2,000", "-2%", delta_color="normal")

st.subheader("Data Display")
st.dataframe(data, use_container_width=True)

st.subheader("Charts")
st.line_chart(data)
st.bar_chart(data)