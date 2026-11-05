from agents import weather_agent
import asyncio
from tools import WeatherDeps

async def main(prompt, **kwargs):
    result = await weather_agent.run(prompt, **kwargs)
    print(result.output)

if __name__ == "__main__":
    asyncio.run(main("Vad är vädret i Stockholm?", deps = WeatherDeps(city="Stockholm")))
