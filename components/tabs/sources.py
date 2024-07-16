import streamlit as st

from pre_index import run
import utils.rag_pipeline as rag
import utils.ollama as ollama

def sources():
    st.title("Directly import your data")
    st.caption("Convert your data into embeddings for utilization during chat")

    data_directory = st.text_input(label="Data directory", value="data")

    if st.button("Process directory"):
        run(data_directory)

        with st.spinner("Processing..."):
            # Initiate the RAG pipeline, providing documents to be saved on disk if necessary
            error = rag.rag_pipeline()

            # Display errors (if any) or proceed
            if error is not None:
                st.exception(error)
            else:
                st.write("Your files are ready. Let's chat! 😎") # TODO: This should be a button.

    st.write("")
    st.caption("Or load the embeddings directory if it's already been created")

    if st.button("Load existing embeddings"):
        with st.spinner("Processing..."):
            # Initiate the RAG pipeline, providing documents to be saved on disk if necessary
            error = rag.rag_pipeline()

            # Display errors (if any) or proceed
            if error is not None:
                st.exception(error)
            else:
                st.write("Your files are ready. Let's chat! 😎") # TODO: This should be a button.

    st.subheader("Chat")
    chat_settings = st.container(border=True)
    with chat_settings:
        st.text_input(
            "Ollama Endpoint",
            key="ollama_endpoint",
            placeholder="http://localhost:11434",
            on_change=ollama.get_models,
        )
        st.selectbox(
            "Model",
            st.session_state["ollama_models"],
            key="selected_model",
            disabled= len(st.session_state["ollama_models"])==0,
            placeholder= "Select Model" if len(st.session_state["ollama_models"])>0 else "No Models Available",
        )
        st.button(
            "Refresh",
            on_click=ollama.get_models,
        )
        st.selectbox(
            "Chat Type",
            options=["Context Only", "Chat Only", "Context and Chat"],
            key="chat_type",
            disabled= len(st.session_state["ollama_models"])==0,
            placeholder= "Select your chat type" if len(st.session_state["ollama_models"])>0 else "No Models Available",
        )
        if st.session_state["advanced"] == True:
            st.select_slider(
                "Top K",
                options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                help="The number of most similar documents to retrieve in response to a query.",
                value=st.session_state["top_k"],
                key="top_k",
            )
            st.text_area(
                "System Prompt",
                value=st.session_state["system_prompt"],
                key="system_prompt",
            )
            st.selectbox(
                "Chat Mode",
                (
                    "compact",
                    "refine",
                    "tree_summarize",
                    "simple_summarize",
                    "accumulate",
                    "compact_accumulate",
                ),
                help="Sets the [Llama Index Query Engine chat mode](https://github.com/run-llama/llama_index/blob/main/docs/module_guides/deploying/query_engine/response_modes.md) used when creating the Query Engine. Default: `compact`.",
                key="chat_mode",
                disabled=True,
            )
            st.write("")