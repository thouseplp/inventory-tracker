import streamlit as st

# Inject custom CSS for the header
st.markdown(
    """
    <style>
    header.st-emotion-cache-1qv137k.eczjsme2 {
        padding-top: 20px;  /* Adjust this for more top padding */
        font-size: 20px;  /* Adjust the size of the header text */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Your original pages dictionary
pages = {
    "Data Upload": [
        st.Page("streamlit_app.py", title="🎯 Closer Targets"),
        st.Page("pages/test3.py", title="🌇 Markets"),
    ],
    "Appointments": [
        st.Page("pages/test.py", title="🌐 Web"),
        st.Page("pages/test2.py", title="🚪 Field"),
    ],
}

# Create navigation
pg = st.navigation(pages)
pg.run()