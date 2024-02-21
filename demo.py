import requests


def get_top_rated_movie():
    api_url = "https://example.com/api/top_rated_movie"
    response = requests.get(api_url)

    if response.status_code == 200:
        json_data = response.json()

        movie_title = json_data.get("title")
        movie_rating = json_data.get("rating")

        if movie_title and movie_rating:
            return movie_title, movie_rating
        else:
            return "Nema dostupnih podataka za film s najvišom ocjenom."
    else:
        return "Došlo je do greške prilikom dohvaćanja podataka."



movie_title, movie_rating = get_top_rated_movie()

print("Film s najvišom ocjenom:")
print(f"Naziv: {movie_title}")
print(f"Ocjena: {movie_rating}")