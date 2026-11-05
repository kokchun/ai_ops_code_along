from pydantic_ai import Agent
from model import nvidia_model
from tools import geocode, get_weather, WeatherDeps
from pydantic_ai.toolsets import FunctionToolset


weather_agent = Agent(
    nvidia_model(),
    instructions=(
        "You are a helpful weather assistant, and always answer "
        "short and concise. Never add more text than neccessary."
        " use the available tools whenever possible. When there "
        " are questions that are not about weather, decline them"
    ),
    toolsets=[FunctionToolset([get_weather, geocode])],
    deps_type=WeatherDeps,
)
