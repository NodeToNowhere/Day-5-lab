# WRITE YOUR FUNCTIONS HERE

#Also using AREPL in VScode, so had to write some data in file. Could probably import data but not sure how within the unit test and 'self' jargon. 

pet_shop_list = [
            {
                "name": "Alice",
                "pets": [],
                "cash": 1000
            },
            {
                "name": "Bob",
                "pets": [],
                "cash": 50
            },
            {
                "name": "Jack",
                "pets": [],
                "cash": 100
            }
        ]
new_pet = {
            "name": "Bors the Younger",
            "pet_type": "cat",
            "breed": "Cornish Rex",
            "price": 100
        }

pet_shop = {
            "pets": [
                {
                    "name": "Sir Percy",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "King Bagdemagus",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "Sir Lancelot",
                    "pet_type": "dog",
                    "breed": "Pomsky",
                    "price": 1000,
                },
                {
                    "name": "Arthur",
                    "pet_type": "dog",
                    "breed": "Husky",
                    "price": 900,
                },
                {
                    "name": "Tristan",
                    "pet_type": "cat",
                    "breed": "Basset Hound",
                    "price": 800,
                },
                {
                    "name": "Merlin",
                    "pet_type": "cat",
                    "breed": "Egyptian Mau",
                    "price": 1500,
                }
            ],
            "admin": {
                "total_cash": 1000,
                "pets_sold": 0,
            },
            "name": "Camelot of Pets"
        }

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    if pet_shop['admin']['total_cash'] >= 0:
        pet_shop['admin']['total_cash'] += cash
    return pet_shop['admin']['total_cash']



def add_or_remove_cash(pet_shop, cash):
    if pet_shop['admin']['total_cash'] >= 0:
        pet_shop['admin']['total_cash'] += cash
    elif pet_shop['admin']['total_cash'] <= 0:
        pet_shop['admin']['total_cash'] -= cash    
    return pet_shop['admin']['total_cash']

print(add_or_remove_cash(pet_shop,10))

def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

print(get_pets_sold(pet_shop))

def increase_pets_sold(pet_shop, sold):
    pet_shop['admin']['pets_sold'] += sold
    return pet_shop['admin']['pets_sold']
    