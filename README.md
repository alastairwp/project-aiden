# Knowledge Hub AI Assistant

## Dependencies
- Python 3.11
- [Ollama](https://ollama.com) installed and set up

## Initial Setup

Run the following commands for initial setup of the system.

### Setting up a Model using Ollama

Once you have Ollama installed, pull the 8b parameter version of Llama3

`ollama pull llama3`

### Setting up your Local Environment

You may need to replace `pip` with `pip3` depending on how your local environment has been set up.

- `pip install pipenv`
- `pipenv install`

## Running the Tool Locally

Make sure you have Ollama running.

Start the Pipenv Shell using

`pipenv shell`

In the Pipenv Shell, run the application

`streamlit run main.py`

## Using the Tool

### Setting up the Model

Scroll down in the left toolbar to set your Ollama endpoint and model. The default endpoint in the tool is set to be the default endpoint of Ollama. If you have pulled Llama3 and are running Ollama, you should see the model in the 'Model' drop-down box and if not, click refresh and it should appear.

### Selecting a Chat Type

Each chat type has a different purpose:

- `Context Only`: The default chat type, only using documents you have added and processed to generate answers and has no general knowledge outside of these documents. Will provide citations to answers.
- `Chat Only`: The default Llama3 model. Has no knowledge of any documents you have added and processed.
- `Context and Chat`: A combination of both the above chat types. Has general knowledge and knowledge of documents you have added and processed.

### Processing Files

If this is the first time you are using the tool, you will need to do the following:
- Create a directory called 'data' in the root of this repository

To add documents to the vector store:
- Copy some PDFs into this data directory
- Click 'Process directory' in the left toolbar
- Wait for the processing to finish and the embeddings directory to be created/updated

### Loading Embeddings

Click the 'Load existing embeddings' button in the left toolbar to load a previously embeddings directory when following the section above.

### Chatting

Once you have either processed files or loaded existing embeddings, chat away 😎