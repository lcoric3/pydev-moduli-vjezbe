from datetime import datetime

def unesi_datum_i_vrijeme():
    unos = input("Unesite datum i vrijeme u formatu 'dd.mm.gggg. hh:mm': ")
    try:
        datum_vrijeme = datetime.strptime(unos, "%d.%m.%Y. %H:%M")
        return datum_vrijeme
    except ValueError:
        print("Neispravan unos. Molimo unesite datum i vrijeme u ispravnom formatu.")
        return None

def ispis_dana(datum_vrijeme):
    dan = datum_vrijeme.day
    print(f"Datum: {dan}.")

def ispis_godine(datum_vrijeme):
    godina = datum_vrijeme.year
    print(f"Godina: {godina}.")

def ispis_sata_i_minuta(datum_vrijeme):
    sati = datum_vrijeme.hour
    minute = datum_vrijeme.minute
    print(f"Sat i minute: {sati}:{minute}.")

def main():
    datum_vrijeme = unesi_datum_i_vrijeme()
    if datum_vrijeme is not None:
        ispis_dana(datum_vrijeme)
        ispis_godine(datum_vrijeme)
        ispis_sata_i_minuta(datum_vrijeme)

if __name__ == "__main__":
    main()