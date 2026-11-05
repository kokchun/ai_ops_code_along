from pydantic_ai import Agent
from dotenv import load_dotenv
from model import nvidia_model
from data_models import ChatRequest, ChatResponse


load_dotenv()

chat_agent = Agent(
    nvidia_model(),
    instructions="Be a joking programming nerd, always answer with a programming joke. Also add in some emojis to make it funnier.",
)

async def chat(request):
    result = await chat_agent.run("message here", message_history="history here")

    return "result.output and all_messages wrapped in a model"
