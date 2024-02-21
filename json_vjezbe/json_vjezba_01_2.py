import json

filename = 'user.json'

with open(filename, 'r') as file:
    user_data = json.load(file)

first_name = user_data['firstName']
last_name = user_data['lastName']
street = user_data['address']['street']
city = user_data['address']['city']
zipcode = user_data['address']['zipcode']

print('Ovo su podaci za dostavu: \n')
print(f'Ime i prezime primatelja: {first_name} {last_name}\n')
print(f'Adresa primatelja: {street},{city} -{zipcode}\n')
