import streamlit as st

icon = ['🌐  ', '🚪  ']
name = ['Web', 'Field Marketing']

with st.sidebar:
    st.markdown("Appointments")
    for i, n in zip(icon, name):
        st.markdown(f"<div style='padding-left: 20px;'>{i} {n}</div>", unsafe_allow_html=True)