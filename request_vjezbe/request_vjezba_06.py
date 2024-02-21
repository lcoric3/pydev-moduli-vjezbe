import requests

def get_movie_info(director_name):

    encoded_director_name = requests.utils.quote(director_name)

    URL = f"https://example.com/api/director_movies?name={encoded_director_name}"
    response = requests.get(URL)

    if response.status_code == 200:
        movies_json = response.json()
        film_titles = movies_json.get('titles')

        if film_titles:
            return film_titles
            
        else:
            print('Ne postoje podaci o filmovima pod trazenim redateljem.')
    else:
        print('Pristup stranici je onemogucen.')




director_name = input('Unesite ime redatelja: ')
movies = get_movie_info(director_name)


print(f'Ovo su filmovi pod trazenim redateljem')
