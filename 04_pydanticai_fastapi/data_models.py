from pydantic import BaseModel, Field
from typing import Literal


class Movie(BaseModel):
    title: str = Field(description="Title of movie")
    year: int = Field(description="Year when this movie came out")
    genre: Literal["action", "comedy", "romance", "cartoon", "adventure"] = Field(
        description="main genre, if there is more than one, choose the one that is most characteristic for the movie"
    )
    rating: int = Field(
        description=(
            "give a rating between 1 and 5, the higher the more popular the movie is "
        ),
        ge=1,
        le=5,
    )
    summary: str = Field(
        description="short exciting summary of the movie, max 3 sentences"
    )
