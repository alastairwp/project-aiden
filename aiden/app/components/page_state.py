# import utils.logs as logs
from app.components.utils.ollama import get_models


def set_initial_state(request):

    ###########
    # General #
    ###########

    if "sidebar_state" not in request.session:
        request.session["sidebar_state"] = "expanded"

    if "ollama_endpoint" not in request.session:
        request.session["ollama_endpoint"] = "http://localhost:11434"

    if "embedding_model" not in request.session:
        request.session["embedding_model"] = "Default (bge-large-en-v1.5)"

    if "ollama_models" not in request.session:
        try:
            models = get_models()
            request.session["ollama_models"] = models
        except Exception:
            request.session["ollama_models"] = []
            pass

    if "selected_model" not in request.session:
        try:
            if "llama3:8b" in request.session["ollama_models"]:
                request.session["selected_model"] = (
                    "llama3:8b"  # Default to llama3:8b on initial load
                )
            elif "llama2:7b" in request.session["ollama_models"]:
                request.session["selected_model"] = (
                    "llama2:7b"  # Default to llama2:7b on initial load
                )
            else:
                request.session["selected_model"] = request.session["ollama_models"][
                    0
                ]  # If llama2:7b is not present, select the first model available
        except Exception:
            request.session["selected_model"] = None
            pass

    if "messages" not in request.session:
        request.session["messages"] = [
            {
                "role": "assistant",
                "content": "Welcome to the Knowledge Hub AI Assistant! To begin, please either select a data directory to process and load, or load an existing embeddings directory. Once you've completed those steps, select a chat type so I can assist you further.",
            }
        ]

    ################################
    #  Files, Documents & Websites #
    ################################

    if "file_list" not in request.session:
        request.session["file_list"] = []

    if "github_repo" not in request.session:
        request.session["github_repo"] = None

    if "websites" not in request.session:
        request.session["websites"] = []

    if "data_directory" not in request.session:
        request.session["data_directory"] = "data"

    ###############
    # Llama-Index #
    ###############

    if "llm" not in request.session:
        request.session["llm"] = None

    if "documents" not in request.session:
        request.session["documents"] = None

    if "query_engine" not in request.session:
        request.session["query_engine"] = None

    if "citation_query_engine" not in request.session:
        request.session["citation_query_engine"] = None

    if "chat_mode" not in request.session:
        request.session["chat_mode"] = "refine"

    if "chat_type" not in request.session:
        request.session["chat_type"] = "Context Only"

    #####################
    # Advanced Settings #
    #####################

    if "advanced" not in request.session:
        request.session["advanced"] = False

    if "system_prompt" not in request.session:
        request.session["system_prompt"] = (
            "You are a sophisticated virtual assistant designed to assist users in comprehensively understanding and extracting insights from a wide range of documents at their disposal. Your expertise lies in tackling complex inquiries and providing insightful analyses based on the information contained within these documents."
        )

    if "top_k" not in request.session:
        request.session["top_k"] = 3

    if "embedding_model" not in request.session:
        request.session["embedding_model"] = None

    if "other_embedding_model" not in request.session:
        request.session["other_embedding_model"] = None

    if "chunk_size" not in request.session:
        request.session["chunk_size"] = 1024

    if "chunk_overlap" not in request.session:
        request.session["chunk_overlap"] = 200
