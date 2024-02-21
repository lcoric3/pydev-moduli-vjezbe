from datetime import datetime 


def unos_datum_i_vrijeme():
    unos = input('Unesi datum i vrijeme u formatu dd.mm.yyyy. hh:mm: ')
    try:
        datum_vrijeme = datetime.strptime(unos, '%d.%m.%Y. %H:%M')
        return datum_vrijeme
    except ValueError:
        print('Neispravan unos. Molimo unesite ispravan format.')
        return None
    
def dan_u_tjednu(datum_vrijeme):
    dani_u_tjednu = ['ponediljak', 'utorak', 'srijeda', 'cetvrtak', 'petak']
    dan_u_tjednu = datum_vrijeme.weekday()
    print(f'Dan u tjednu: {dani_u_tjednu[dan_u_tjednu]}')

def main():
    datum_vrijeme = unos_datum_i_vrijeme()
    if datum_vrijeme is not None:
        dan_u_tjednu(datum_vrijeme)

if __name__ == '__main__':
    main()