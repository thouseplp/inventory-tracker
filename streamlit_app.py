import streamlit as st
from streamlit_option_menu import option_menu

# Define the on_change callback function
def on_change():
    selection = st.session_state['sidebar_menu']
    st.write(f"Selection changed to {selection}")

# Create a vertical option menu in the sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Data Upload",  # Required parameter
        options=["Closer Targets", "Upload", "Tasks", "Settings"],  # Menu options
        icons=["house", "cloud-upload", "list-task", "gear"],  # Icons for each option
        menu_icon="cast",  # Icon for the menu title
        default_index=0,  # Index of the initially selected option
        on_change=on_change,  # Callback function
        key='sidebar_menu',  # Key for the menu's state in session_state
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},  # Transparent background
            "icon": {"color": "white", "font-size": "20px"},  # Icon style
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "color": "white", "--hover-color": "#FFFFFF"},  # Link style
            "nav-link-selected": {"background-color": "#FFffff", "color": "white"},  # Selected link style
        }
    )

# Display the selected option
st.write(f"You selected: {selected}")