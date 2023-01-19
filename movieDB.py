import requests
import sys
from dotenv import load_dotenv
import os

page = 0
i = 1
MOVIEDB_API_KEY = os.getenv("MOVIEDB_API_KEY")

def main():
    configure()

    # Primary program loop
    numofmovies = userinput()
    while True:
        urlupdate()
        printmovies(numofmovies)
        continue

# Introduces the API url. Preps it to be updated depending on how many pages are needed to execute the program

def urlupdate():
    global movie_list
    global page

    # Iterates the page up by one every time the loop restarts
    page += 1
    
    # API URL to the most popular movies, updates daily
    api_url = f"https://api.themoviedb.org/3/movie/popular?api_key={os.getenv('api_key')}&language=en-US&page={str(page)}"
    response = requests.get(api_url)
    
    # Assigns movie_list to the results from API URL, returns it as a JSON (turned into a dict)
    movie_list = response.json()

# Prints the inputted number of movies. 

def printmovies(n):
    global i
    global page

    while i - 20 <= n:
            if i - page * 20 < 0:
                i += 20
                try:
                    print(movie_list["results"][i - page * 20 - 1]["original_title"])
                except IndexError:
                    break
                else:
                    i += 1 
                    print(i - 21)
            else:
                try:
                    print(movie_list["results"][i - page * 20 - 1]["original_title"])
                except IndexError:
                    break 
                else:
                    i += 1 
                    print(i - 21)
    if i - 20 == n + 1:
            print(movie_list["results"][i - page * 20 - 1]["original_title"])      
            sys.exit()

def userinput():
    while True:
        try:
            numofmovies = int(input("How many movies would you like recommended?\n"))
        except (TypeError, ValueError):
            print("Please input an integer.")
        else:
            return numofmovies

def configure():
    load_dotenv()

main()