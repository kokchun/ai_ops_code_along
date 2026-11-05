from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    question: str
    message_history: list 
    ...


class ChatResponse(BaseModel):
    response: str 
    message_history: list
    ...