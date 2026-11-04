from agents import movie_agent
from fastapi import FastAPI

app = FastAPI()

@app.get("/movies")
async def read_movies():
    # TODO: implement this 
    return "movies here testing reload"

@app.post("/movie")
async def create_movie(query: str):
    result = await movie_agent.run(query)
    # TODO: save to database

    return result.output