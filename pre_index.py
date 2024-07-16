import sys
import os
from typing import List
import shutil
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.storage.storage_context import StorageContext
import utils.logs as logs

EMBEDDINGS_DIRECTORY = os.getcwd() + "/embeddings"
# TEMP_DIRECTORY = os.getcwd() + "/temp"
# storage_context = StorageContext.from_defaults(persist_dir=embeddingsDir)


FORMATS = [
    #"csv",
    "docx",
    "epub",
    "ipynb",
    #"json",
    "md",
    "pdf",
    "ppt",
    "pptx",
    "txt",
]

EMBEDDING_MODEL = 'BAAI/bge-large-en-v1.5'

def init(data_directory: str):
    # index_directory = sys.argv[1]
    
    init_model()

    print("Loading files from " + data_directory + " directory")

    if os.path.exists(EMBEDDINGS_DIRECTORY):
        storage_context = StorageContext.from_defaults(persist_dir=EMBEDDINGS_DIRECTORY)
        index = load_index_from_storage(storage_context)

        documents = SimpleDirectoryReader(data_directory, filename_as_id=True).load_data(show_progress = True)

        refreshed_index = index.refresh_ref_docs(documents=documents)

        # logs.log.info(f"Refreshed documents: {refreshed_index}")

        index.storage_context.persist(EMBEDDINGS_DIRECTORY)

        print("Saved index to: " + EMBEDDINGS_DIRECTORY + "/")

        del documents
    
    else:
        create_dir(EMBEDDINGS_DIRECTORY)
        # create_dir(TEMP_DIRECTORY)

        list_of_files = [f for f in os.listdir(data_directory) if os.path.isfile(os.path.join(data_directory, f))]
        list_of_files = get_valid_file_formats(list_of_files, FORMATS)

        # for file in list_of_files:
        #     shutil.copyfile(data_directory + "/" + file, TEMP_DIRECTORY + "/" + file)

        del list_of_files

        documents = SimpleDirectoryReader(data_directory, filename_as_id=True).load_data(show_progress = True)

        index = VectorStoreIndex.from_documents(documents, show_progress=True)

        index.storage_context.persist(EMBEDDINGS_DIRECTORY)

        print("Saved index to: " + EMBEDDINGS_DIRECTORY + "/")

        del documents

def create_dir(dir: str) -> None:
    if not os.path.exists(dir):
        os.makedirs(dir)
    

def get_valid_file_formats(files: List[str], formats: List[str]) -> List[str]:
    out = []
    for file in files:
        extension = file.split(".")[-1]
        if extension in formats:
            out.append(file)
    return out

def init_model() -> None: 
    try:
        from torch import cuda
        device = "cpu" if not cuda.is_available() else "cuda"
    except:
        device = "cpu"

    Settings.embed_model = HuggingFaceEmbedding(
        model_name=EMBEDDING_MODEL,
        device=device,
    )

def run(data_directory: str) -> None:
    try:
        init(data_directory)
    except Exception as e:
        raise Exception(e)
    # finally:
    #     shutil.rmtree(TEMP_DIRECTORY)

# if __name__ == "__main__":
#     """
#     Load example:

#     initModel()
#     from llama_index.core import load_index_from_storage
#     index = load_index_from_storage(storage_context)
#     print(index.docstore.docs.values())
#     """
    
#     try:
#         init()
#     finally:
#         shutil.rmtree(TEMP_DIRECTORY)