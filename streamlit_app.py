import streamlit as st

pages = {
    "Your account": [
        st.Page("streamlit_app.py", title="Create your account"),
        st.Page("pages/test3.py", title="Manage your account"),
    ],
    "Resources": [
        st.Page("pages/test.py", title="Learn about us"),
        st.Page("pages/test2.py", title="Try it out"),
    ],
}

pg = st.navigation(pages)
pg.run()