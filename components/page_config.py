import streamlit as st
from PIL import Image

mercator_logo = Image.open("components/images/mercator_digital_logo.jpeg")

def set_page_config():
    st.set_page_config(
        page_title="Knowledge Hub AI Assistant",
        page_icon=mercator_logo,
        layout="wide",
        initial_sidebar_state=st.session_state["sidebar_state"]
    )

    # Remove the Streamlit `Deploy` button from the Header
    st.markdown(
        r"""
    <style>
    .stDeployButton {
            visibility: hidden;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
