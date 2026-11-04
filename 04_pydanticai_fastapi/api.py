from agents import movie_agent
from fastapi import FastAPI

app = FastAPI()

@app.get("/movies")
async def read_movies():
    # TODO: implement this 
    return "movies here"
