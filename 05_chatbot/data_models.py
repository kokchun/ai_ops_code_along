from pydantic import BaseModel, Field
from pydantic_ai import ModelMessage

class ChatRequest(BaseModel):
    question: str = Field(description="a message to the agent")
    message_history: list[ModelMessage] = Field(description="a list of model messages")


class ChatResponse(BaseModel):
    response: str = Field(description="response from the agent")
    message_history: list[ModelMessage] = Field(description="a list of model messages")
