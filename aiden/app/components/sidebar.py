import streamlit as st

from aiden.app.components.tabs.sources import sources
from aiden.app.components.tabs.settings import settings


def sidebar():
    with st.sidebar:
        tab1, tab2 = st.sidebar.tabs(["Data Sources", "Settings"])

        with tab1:
            sources()

        with tab2:
            settings()
