import json

user = { "id": 1, 
        "firstName": "Petar", 
        "lastName": "Peric", 
        "username": "pperic", 
        "email": "pperic@email.com", 
        "address": { 
            "street": "Ilica 256", 
            "city": "Zagreb", 
            "zipcode": "10000"
        }, 
        "phone": "+385 1 8031 564", 
        "website": "web.adresa", 
        "company": { 
            "name": "Medvednica d.o.o.", 
            "catchPhrase": "Razvoj specijaliziranih Python aplikacija", 
            "bs": "Najbolja poslovna rjesenja" 
        } 
        
}

filename = 'user.json'

with open(filename, 'w') as file:
    json.dump(user, file, indent=4)
