import requests


URL = "https://example.com/api/top_rated_movie"

response = requests.get(URL)

if response.status_code == 200:
    movie_json = response.json()
    movie_title = movie_json.get('title')
    movie_rating = movie_json.get('rating')

    if movie_title and movie_rating:
        print (f'Ime filma: {movie_title}\n,Ocjena: {movie_rating}')
    else:
        print('Nema informacija o filmu.')

else:
    print('Pristup stranici je onemogucen.')
    
