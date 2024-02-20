from film import Movie
from film_api import get_movie_info, write_to_csv

def main():
    # Stvaranje objekta filma
    film = Movie("The Shawshank Redemption", 1994, "Frank Darabont", 9.3)

    # Prikaz informacija o filmu
    film.display_info()

    # Spremanje informacija o filmu u datoteku
    Movie.save_to_file(film, "film.txt")

    # Učitavanje informacija o filmu iz datoteke
    ucitani_film = Movie.load_from_file("film.txt")
    ucitani_film.display_info()

    movie_info = get_movie_info(film)
    if movie_info:
        print("Informacije o filmu:")
        print(f"Naslov: {movie_info['title']}")
        print(f"Godina: {movie_info['year']}")
        print(f"Redatelj: {movie_info['director']}")
        print(f"Ocjena: {movie_info['rating']}")

        # Pisanje u csv datoteku
        write_to_csv(movie_info, "filmovi.csv")
        print("Informacije su zapisane u datoteku 'filmovi.csv' ")
    else:
        print("Nije moguce pronaci informacije o filmu.")


 
if __name__ == "__main__":
    main()