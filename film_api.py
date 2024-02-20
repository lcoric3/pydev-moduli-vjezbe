
import requests
import csv

def get_movie_info(movie_title):
    # Dohvaćanje informacija o filmu iz API-ja
    url = f"https://api.example.com/movies/{movie_title}"
    response = requests.get(url)

    if response.status_code == 200:
        movie_info = response.json()
        return movie_info
    else:
        return None

def write_to_csv(movie_info, filename):
    # Pisanje informacija o filmu u CSV datoteku
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Year', 'Director', 'Rating'])
        writer.writerow([movie_info['title'], movie_info['year'], movie_info['director'], movie_info['rating']])

        