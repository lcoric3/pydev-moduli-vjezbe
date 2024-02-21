import requests
import json
import sqlite3
from bs4 import BeautifulSoup


class Country:
    def __init__(self, name, capital, population, area):
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area

    def __repr__(self):
        return f"Country(name='{self.name}', capital='{self.capital}', population={self.population}, area={self.area})"



url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
json_data = response.json()

countries = []
for data in json_data:
    country = Country(data["country"], data["capital"], data["population"], data["area"])
    countries.append(country)

largest_country = max(countries, key=lambda c: c.area)
smallest_country = min(countries, key=lambda c: c.area)

most_populous_country = max(countries, key=lambda c: c.population)
least_populous_country = min(countries, key=lambda c: c.population)



filename_txt = "countries.txt"
with open(filename_txt, "w") as file:
    for country in countries:
        file.write(str(country) + "\n")

filename_json = "countries.json"
with open(filename_json, "w") as file:
    json.dump([country.__dict__ for country in countries], file, indent=4)


    
conn = sqlite3.connect("countries.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS countries
                  (name TEXT, capital TEXT, population INTEGER, area REAL)''')

for country in countries:
    cursor.execute("INSERT INTO countries VALUES (?, ?, ?, ?)",
                   (country.name, country.capital, country.population, country.area))

conn.commit()
conn.close()



print("Najveća država na svijetu:", largest_country)
print("Najmanja država na svijetu:", smallest_country)
print("Država s najviše stanovnika:", most_populous_country)
print("Država s najmanje stanovnika:", least_populous_country)
print("Podaci su spremljeni u datoteke:", filename_txt, "i", filename_json)
print("Podaci su spremljeni u SQLite bazu podataka: countries.db")