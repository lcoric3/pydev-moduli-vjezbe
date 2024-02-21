import requests


def get_movie_info(title):

    encoded_title =  requests.utils.quote(title)
    
    URL = f"https://example.com/api/search?title={encoded_title}"
    
    response = requests.get(URL)
    
    if response.status_code == 200:
        movie_json = response.json()

        movie_data = movie_json.get('film')

        if movie_data:
            realse_year = movie_data.get("realase_year")

            if realse_year:
                return realse_year
            else:
                return 'Nema dostupnih informacija o izlazku filma'
        else:
            return 'Film nije pronaden'
    else:
        return 'Doslo je do greske prilikom pristupa stranici.'

movie_title = input('Unesite naziv filma: ')
film_year = get_movie_info(movie_title)
print(f"Godina izlazka filma '{movie_title}' : {film_year}")