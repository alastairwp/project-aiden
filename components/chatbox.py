import streamlit as st

from utils.ollama import chat, context_chat, citation_chat
import utils.logs as logs


def chatbox():
    if prompt := st.chat_input("How can I help?"):
        # Prevent submission if Ollama endpoint is not set
        if not st.session_state["query_engine"] and st.session_state["chat_type"] != "Chat Only":
            st.warning("Please confirm settings and upload files before proceeding.")
            st.stop()

        # Add the user input to messages state
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate llama-index stream with user input
        with st.chat_message("assistant"):
            with st.spinner("Processing..."):
                if st.session_state["chat_type"] == "Chat Only":
                    response = st.write_stream(
                        chat(prompt=prompt)
                    )
                elif st.session_state["chat_type"] == "Context and Chat":
                    response = st.write_stream(
                        context_chat(
                            prompt=prompt, query_engine=st.session_state["query_engine"]
                        )
                    )
                elif st.session_state["chat_type"] == "Context Only":
                    response = st.write_stream(
                        citation_chat(
                            prompt=prompt, query_engine=st.session_state["citation_query_engine"]
                        )
                    )
                else:
                    invalid_chat_type = st.session_state["chat_type"]
                    logs.log.error(f"Invalid chat type: {invalid_chat_type}")
                    raise KeyError(f"Invalid chat type: {invalid_chat_type}")

        # Add the final response to messages state
        st.session_state["messages"].append({"role": "assistant", "content": response})
