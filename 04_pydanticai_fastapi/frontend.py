import requests
import streamlit as st
import pandas as pd
# from api import create_movie, read_movies -> tightly coupled


def layout():
    st.markdown("# Cool Movies")

    movie_string = st.text_input("Give a statement and it will give backa movie")

    movie = requests.post("http://127.0.0.1:8000/movie", json={"prompt": movie_string}).json()

    if movie:
        st.write(movie)

    genre = st.selectbox(
        "Choose genre", options=["action", "comedy", "cartoon", "adventure", "romance"]
    )

    movies = requests.get(f"http://127.0.0.1:8000/movies?genre={genre}").json()

    st.dataframe(movies)


if __name__ == "__main__":
    layout()
