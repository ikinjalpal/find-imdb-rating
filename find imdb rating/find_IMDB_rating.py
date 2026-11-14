import requests
import pandas as pd
import os

API_KEY = "ee24cebf" 

# List contaiting all the films for which data has to be scraped from IMDB
films = []

# Lists contaiting web scraped data
names = []
ratings = []
genres = []

# Define path where your films are present 
# For eg: "/Users/utkarsh/Desktop/films"
path = input("Enter the path where your films are: ")

# Films with extensions
for film in os.listdir(path):
    films.append(os.path.splitext(film)[0])

for title in films:
    try:
        response = requests.get("https://www.omdbapi.com/", params={"t": title, "apikey": API_KEY},timeout=10,)
        data = response.json()
        print(data)
        

        if data.get("response") == "True":
            names.append(data["Title"])
            ratings.append(data["imdbRating"])
            genres.append(data["Genre"])
        else:
            print(f"Not Found {title} ({data.get('Error')})")
    except Exception as e:
        print(f"Error for {title}: {e}")

df = pd.DataFrame({"Film Name": names, "Rating": ratings, "Genre": genres})
print(df)


df.to_csv("film ratings.csv", index=False, encoding="utf-8")


