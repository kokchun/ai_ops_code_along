from fastapi import FastAPI
from chat_agent import chat
from data_models import ChatResponse, ChatRequest

app = FastAPI()

# get endpoint to pick out chat history

@app.post("/chat", response_model=ChatResponse)
async def joke_chat(request: ChatRequest):
    chat_response = await chat(request=request)

    # logic to store chat in database
    # ...
    
    return chat_response
