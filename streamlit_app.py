import streamlit as st

test = ['Test', 'Cat']

with st.sidebar:
    st.header("Test")
    for i in test:
        st.markdown(f"<div style='padding-left: 20px; font-size: 35px'>{i}</div>", unsafe_allow_html=True)
