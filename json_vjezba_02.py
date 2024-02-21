import requests 
import json

URL = "https://jsonplaceholder.typicode.com/users" 

response = requests.get(URL)
data = response.json()

filename = 'users.json'

with open(filename, 'w') as file:
    json.dump(data, file, indent=4)

users_dict = {}
for user in data:
    user_id = user['id']
    first_name = user['name'].split()[0]
    last_name = user['name'].split()[1]
    phone = user['phone']
    users_dict[user_id] = {'ime': first_name, 'prezime': last_name, 'phone': phone}

filename_txt = 'users.txt'

with open(filename_txt, 'w') as file:
    for user_id, user_data in users_dict.items():
        file.write(f'ID: {user_id}\n')
        file.write(f'Ime: {user_data['ime']}\n')
        file.write(f'Prezime: {user_data['prezime']}\n')
        file.write(f'Broj: {user_data['phone']}\n')
        file.write(f'\n')