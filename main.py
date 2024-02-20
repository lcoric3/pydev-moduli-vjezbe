from film import Movie
from film_api import get_movie_info, write_to_csv
from film_datebase import FilmDateBase

def main():
      # Stvaranje instance baze podataka
    db = FilmDateBase("filmovi.db")

    while True:
        # Ispis opcija
        print("Odaberite opciju:")
        print("1. Dodaj film")
        print("2. Ažuriraj film")
        print("3. Ukloni film")
        print("4. Prikaz svih filmova")
        print("5. Izlaz")

        opcija = input("Unesite broj opcije: ")

        if opcija == "1":
            # Unos informacija o filmu
            naslov = input("Unesite naslov filma: ")
            godina = input("Unesite godinu filma: ")
            redatelj = input("Unesite ime redatelja: ")
            ocjena = input("Unesite ocjenu filma: ")

            # Dodavanje filma u bazu podataka
            db.dodaj_film(naslov, godina, redatelj, ocjena)
            print("Film je dodan u bazu podataka.")

        elif opcija == "2":
            # Unos ID-a filma za ažuriranje
            film_id = input("Unesite ID filma koji želite ažurirati: ")

            # Provjera postojanja filma u bazi podataka
            if db.provjeri_film(film_id):
                # Unos novih informacija o filmu
                naslov = input("Unesite novi naslov filma: ")
                godina = input("Unesite novu godinu filma: ")
                redatelj = input("Unesite novo ime redatelja: ")
                ocjena = input("Unesite novu ocjenu filma: ")

                # Ažuriranje filma u bazi podataka
                db.azuriraj_film(film_id, naslov, godina, redatelj, ocjena)
                print("Film je ažuriran.")

            else:
                print("Film s unesenim ID-om ne postoji.")

        elif opcija == "3":
            # Unos ID-a filma za uklanjanje
            film_id = input("Unesite ID filma koji želite ukloniti: ")

            # Uklanjanje filma iz baze podataka
            db.ukloni_film(film_id)
            print("Film je uklonjen iz baze podataka.")

        elif opcija == "4":
            # Prikaz svih filmova iz baze podataka
            filmovi = db.prikazi_filmove()

            if filmovi:
                print("Popis svih filmova:")
                for film in filmovi:
                    print(film)
            else:
                print("Baza podataka je prazna.")

        elif opcija == "5":
            # Zatvaranje veze s bazom podataka
            db.zatvori_bazu()
            break

        else:
            print("Neispravna opcija. Molimo odaberite ponovno.")


   
 


 


if __name__ == "__main__":
    main()