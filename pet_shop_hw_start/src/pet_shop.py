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


def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']


def increase_pets_sold(pet_shop, sold):
    pet_shop['admin']['pets_sold'] += sold
    
    
def get_stock_count(pet_shop):
    return len(pet_shop['pets']) 

def get_pets_by_breed(pet_shop, breed):
    pets = []
    for animals in (pet_shop['pets']):
        if animals['breed'] == breed:
            pets.append(breed)
    return pets

 #hours and hours of issues with find and remove name... != None, KeyErrors... no idea. Wish i'd started sooner as i've spent hours on something I could have just asked about in chat two days ago..
 
def find_pet_by_name(pet_shop, name):
    for pet in (pet_shop['pets']):
        if pet['name'] == name:
            return name
    else:
        return None            

def remove_pet_by_name(pet_shop, name):         
    index = 0
    for pet in pet_shop['pets']:
        if pet['name'] == name:
            # print(pet)
            del pet_shop['pets'][index]
        else:
            index += 1
#fucking index... omfg

# print(pet_shop['pets'][3])
# find_pet_by_name(pet_shop, 'Arthur')
# remove_pet_by_name(pet_shop, "Arthur")
# find_pet_by_name(pet_shop, "Arthur")
# print(pet_shop['pets'][3])

def add_pet_to_stock(pet_shop, stock):
    pet_shop['pets'].append(stock)
   
def get_customer_cash(customer):
        return customer['cash']
        
def remove_customer_cash(customer, cost):
    customer['cash'] -= cost


def get_customer_pet_count(customer):
    return len(customer['pets'])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

    # --- OPTIONAL ---

def customer_can_afford_pet(customer, pet):
    if customer['cash'] >= pet['price']:
        return True
    else:
        return False

    
def sell_pet_to_customer(pet_shop, pet, customer):
    add_pet_to_customer(customer, pet)
    increase_pets_sold(pet_shop, 1)
    add_or_remove_cash(pet_shop, 900)
    remove_customer_cash(pet_shop, 900)
    get_total_cash(pet_shop)
# customer = customers[0]  
# print(sell_pet_to_customer(pet_shop, find_pet_by_name(pet_shop, "Arthur"),customers[0]))
    