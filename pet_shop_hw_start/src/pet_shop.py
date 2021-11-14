# WRITE YOUR FUNCTIONS HERE

#Also using AREPL in VScode, so had to write some data in file. Could probably import data but not sure how within the unit test and 'self' jargon. 

#ask about consistently storing local vars and using them to return output. Better to be specific? 

#ex 
# def get_pets_sold(pet_shop):
#     return pet_shop['admin']['pets_sold']

# def get_pets_sold(pet_shop):
#     sold = 0
#     sold += pet_shop['admin']['pets_sold'] 
#     return sold

customers = [
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
    pet_shop['admin']['total_cash'] += cash
    return pet_shop['admin']['total_cash']


def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']


def increase_pets_sold(pet_shop, sold):
    pet_shop['admin']['pets_sold'] += sold
    return pet_shop['admin']['pets_sold']
    
def get_stock_count(pet_shop):
    return len(pet_shop['pets']) 

def get_pets_by_breed(pet_shop, breed):
    pets = []
    for animals in (pet_shop['pets']):
        if animals['breed'] == breed:
            pets.append(breed)
    return pets

def find_pet_by_name(pet_shop, name):
    for pet in (pet_shop['pets']):
        if pet['name'] == name:       
            return pet['name']
    else:
        return None    
        
def remove_pet_by_name(pet_shop,name):
    for pet in (pet_shop['pets']):
        if pet['name'] == name:  
            del pet     

def add_pet_to_stock(pet_shop, stock):
    pet_shop['pets'].append(stock)
   
def get_customer_cash(customer):
        return customer['cash']
        
def remove_customer_cash(customer, cost):
    customer['cash'] -= cost
    return customer['cash']


def get_customer_pet_count(customer):
    return len(customer['pets'])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

    