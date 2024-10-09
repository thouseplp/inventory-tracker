import streamlit as st

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

pg = st.navigation(pages)
pg.run()