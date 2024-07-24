from django.shortcuts import render
from django.http import HttpRequest
from app.components.page_state import set_initial_state
from app.components.utils.ollama import chat, context_chat, citation_chat
import ollama


def home(request):
    assert isinstance(request, HttpRequest)
    set_initial_state(request)
    if request.method == "POST":
        prompt = request.POST.get('inputPrompt')
        
       
      #  llm = create_ollama_llm(
      #      "llama3:8b",
      #      "http://localhost:11434",
      #  )
      #  stream = llm.stream_complete(prompt)
      #  for chunk in stream:
      #      yield chunk.delta
    
    #for msg in request.session["messages"]:
    #    chat_messages = msg["role"] + ": " + msg["content"]
   
    return render(
        request,
        'home.html',
        {
        
            # 'response' : response       
        }
    )