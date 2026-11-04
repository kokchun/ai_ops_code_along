from agents import movie_agent
from fastapi import FastAPI
from setup_db import query_duckdb
from data_models import Prompt

app = FastAPI()


@app.get("/movies")
async def read_movies(genre: str | None = None):

    if genre:
        sql = "SELECT * FROM movies WHERE genre = ?;"
        params = [genre]
    if genre == "all" or not genre: 
        sql = "FROM movies;"
        params = None


    movies = query_duckdb(sql, parameters=params)
    return movies.to_dict(orient="records")


@app.post("/movie")
async def create_movie(query: Prompt):
    result = await movie_agent.run(query.prompt)

    movie = result.output

    query_duckdb(
        "INSERT INTO movies VALUES (?,?,?,?,?)",
        parameters=[movie.title, movie.year, movie.genre, movie.rating, movie.summary],
    )

    return movie
