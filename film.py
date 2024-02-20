class Movie:
    def __init__(self, title, year, director, rating):
        self.title = title
        self.year = year
        self.director = director
        self.rating = rating

    def display_info(self):
        print(f"Naslov filma: {self.title}")
        print(f"Godina: {self.year}")
        print(f"Redatelj: {self.director}")
        print(f"Ocjena: {self.rating}")

    @staticmethod
    def save_to_file(movie, file):
        with open(file, 'w') as f:
            f.write(f"Naslov: {movie.title}\n")
            f.write(f"Godina: {movie.year}\n")
            f.write(f"Redatelj: {movie.director}\n")
            f.write(f"Ocjena: {movie.rating}\n")

    @staticmethod
    def load_from_file(file):
        with open(file, 'r') as f:
            title = f.readline().strip().split(': ')[1]
            year = f.readline().strip().split(': ')[1]
            director = f.readline().strip().split(': ')[1]
            rating = f.readline().strip().split(': ')[1]
            return Movie(title, year, director, rating)

film = Movie("The Shawshank Redemption", 1994, "Frank Darabont", 9.3)

# Prikaz informacija o filmu
film.display_info()

# Spremanje informacija o filmu u datoteku
Movie.save_to_file(film, "film.txt")


# Učitavanje informacija o filmu iz datoteke
ucitani_film = Movie.load_from_file("film.txt")
ucitani_film.display_info()
