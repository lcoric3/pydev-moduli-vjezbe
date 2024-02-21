from datetime import datetime, timedelta



class OlympicGames:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def get_opening_ceremony_day(self):
        return self.start_date.strftime("%A")

    def get_closing_ceremony_day(self):
        return self.end_date.strftime("%A")

    def get_days_until_start(self):
        today = datetime.today().date()
        days_until_start = (self.start_date.date() - today).days
        return days_until_start

    def get_days_until_end(self):
        today = datetime.today().date()
        days_until_end = (self.end_date.date() - today).days
        return days_until_end

    def get_time_until_start(self, location):
        now = datetime.now()
        start_datetime = datetime.combine(self.start_date.date(), now.time())
        time_until_start = start_datetime - now
        return time_until_start, location

    
    
def main():
    # Definiranje datuma Olimpijskih igara
    start_date = datetime(2021, 7, 23)
    end_date = datetime(2021, 8, 8)

    # Stvaranje instance klase OlympicGames
    olympics = OlympicGames(start_date, end_date)

    # Ceremonija otvaranja
    opening_ceremony_day = olympics.get_opening_ceremony_day()
    print("Ceremonija otvaranja je u {}.".format(opening_ceremony_day))

    # Ceremonija zatvaranja
    closing_ceremony_day = olympics.get_closing_ceremony_day()
    print("Ceremonija zatvaranja je u {}.".format(closing_ceremony_day))

    # Broj dana do početka
    days_until_start = olympics.get_days_until_start()
    print("Do početka OI ima {} dana.".format(days_until_start))

    # Broj dana do završetka
    days_until_end = olympics.get_days_until_end()
    print("Do završetka OI ima {} dana.".format(days_until_end))

    # Vremenski razmak do početka u različitim gradovima
    locations = {
        "Tokio": timedelta(hours=9),
        "Melbourne": timedelta(hours=10),
        "Dubai": timedelta(hours=4),
        "Moskva": timedelta(hours=3),
        "Zagreb": timedelta(hours=2),
        "London": timedelta(hours=1),
        "New York": timedelta(hours=-4),
        "Los Angeles": timedelta(hours=-7)
    }

    for location, offset in locations.items():
        time_until_start, location = olympics.get_time_until_start(location)
        local_start_time = datetime.now() + offset + time_until_start
        days_hours_until_start = divmod(time_until_start.total_seconds(), 3600 * 24)
        print("Do početka OI u {} ima {} dana i {} sati.".format(location, int(days_hours_until_start[0]), int(days_hours_until_start[1])))

        
        
        
if __name__ == "__main__":
    main()