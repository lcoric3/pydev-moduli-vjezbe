import requests


URL =  "https://example.com/api/popular_movies?year=2022"

response = requests.get(URL)

if response.status_code == 200:
    movie_data = response.json()

    movies_title = movie_data.get('movies')
   
   

    if movies_title:
        print('Najpopularniji filmovi u 2022.godini:')
        for movie in movies_title:
            film_title = movie.get('title')
            print(film_title)

    else:
        print('Nema podataka o tim filmovima.')

else:
    print('Dogodila se greska prilikom spajanja na stranicu.')
        
