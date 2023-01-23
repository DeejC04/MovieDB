import os
from dotenv import load_dotenv
import requests

def configure():
    load_dotenv()

def urlupdate(page):
    api_url = f"https://api.themoviedb.org/3/movie/popular?api_key={os.getenv('api_key')}&language=en-US&page={str(page)}"
    response = requests.get(api_url)
    return response.json()

def get_movies(n):
    i = 1
    page = 1
    recommended_movies = []
    while len(recommended_movies) < n:
        movie_list = urlupdate(page)
        for i in range(len(movie_list["results"])):
            if len(recommended_movies) >= n:
                break
            recommended_movies.append(movie_list["results"][i]["original_title"])
        page += 1
    return recommended_movies


