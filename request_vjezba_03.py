import requests


URL = "https://example.com/api/film/123456"

response = requests.get(URL)

if response.status_code == 200:
    movie_json = response.json()
    
    movie_title = movie_json.get('title')

    if movie_title:
        print(f'Naziv filma koji smo trazili: {movie_title}')
    else:
        print('Podaci o filmu nisu pronadeni.')
else:
    print('Doslo je do greske prilikom spajanja na trazenu adresu.')