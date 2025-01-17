import time
import streamlit as st

from aiden.app.components.chatbox import chatbox
from aiden.app.components.header import set_page_header
from aiden.app.components.sidebar import sidebar

from aiden.app.components.page_config import set_page_config
from aiden.app.components.page_state import set_initial_state


def generate_welcome_message(msg):
    for char in msg:
        time.sleep(0.025)  # TODO: Find a better way -- This is blocking :(
        yield char


### Setup Initial State
set_initial_state()

### Page Setup
# set_page_config()
# set_page_header()

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])
    # st.chat_message(msg["role"]).write_stream(generate_welcome_message(msg['content']))

### Sidebar
# sidebar()

### Chat Box
# chatbox()
