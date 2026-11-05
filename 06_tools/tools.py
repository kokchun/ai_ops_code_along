import httpx
from dataclasses import dataclass
from pydantic_ai import RunContext

@dataclass
class WeatherDeps:
    city: str



 