import streamlit as st

# Inject custom CSS to remove the border around st.expander
hide_expander_border = """
    <style>
    [data-testid="stExpander"] details {
        border: none !important;
    }
    </style>
"""

# Inject the CSS into the app
st.markdown(hide_expander_border, unsafe_allow_html=True)

custom_css = """
    <style>
    [data-testid="stExpander"] details {
        font-size: 4rem !important;
    }
    </style>
"""

# Inject the CSS into the app
st.markdown(custom_css, unsafe_allow_html=True)

# Example of expander with larger label text
with st.sidebar:
    with st.expander("Larger Label Text", expanded=True):
        st.write("      This expander label is larger.")