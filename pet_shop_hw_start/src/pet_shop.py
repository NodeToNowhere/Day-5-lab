# WRITE YOUR FUNCTIONS HERE

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
            del pet_shop['pets'][index]
        else:
            index += 1


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
    remove_customer_cash(customer, 900)
    get_total_cash(pet_shop)


    