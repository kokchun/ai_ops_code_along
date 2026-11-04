from agents import movie_agent
from fastapi import FastAPI
from setup_db import query_duckdb

app = FastAPI()


@app.get("/movies")
async def read_movies():
    movies = query_duckdb("FROM movies;")
    return movies.to_dict(orient="records")


@app.post("/movie")
async def create_movie(query: str):
    result = await movie_agent.run(query)

    movie = result.output

    query_duckdb(
        "INSERT INTO movies VALUES (?,?,?,?,?)",
        parameters=[movie.title, movie.year, movie.genre, movie.rating, movie.summary],
    )

    return movie
