from film import Movie

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

if __name__ == "__main__":
    main()