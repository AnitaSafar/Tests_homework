# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(best_shop):
    return(best_shop["name"])

def get_total_cash(money):
    return(money["admin"]["total_cash"])

def add_or_remove_cash(total, change):
    total["admin"]["total_cash"] = total["admin"]["total_cash"] + change
    return total["admin"]["total_cash"]

def get_pets_sold(lucky):
    return(lucky["admin"]["pets_sold"])

def increase_pets_sold(lucky, amount):
    lucky["admin"]["pets_sold"] = lucky["admin"]["pets_sold"] + amount
    return(lucky["admin"]["pets_sold"])

def get_stock_count(available_pets):
    return(len(available_pets["pets"]))

def get_pets_by_breed(animals, shorthair):
    sum = []
    for cat in animals["pets"]:
        if cat["breed"] == shorthair:
            sum.append(sum)
    return sum

def get_pets_by_breed(animals, dalmation):
    sum = []
    for dog in animals["pets"]:
        if dog["breed"] == dalmation:
            sum.append(sum)
    return sum
        

def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return(pet)


def find_pet_by_name_none(animals, fred):
    for missing in animals["pets"]:
        if missing["name"] != fred:
            return(None)


def remove_pet_by_name(remove, fav):
    for husky in remove["pets"]:
        if husky["name"] == fav:
            remove["pets"].remove(husky)
            return(remove["pets"])


def add_pet_to_stock(add_stock, addition):
    add_stock["pets"].append(addition)
    return(len(add_stock["pets"]))


def get_customer_cash(customer):
    return(customer["cash"])


def remove_customer_cash(best_customer, amount):
    best_customer["cash"] = best_customer["cash"] - amount
    return best_customer["cash"]


def get_customer_pet_count(happy):
    return(len(happy["pets"]))


def add_pet_to_customer(bought, cat):
    bought["pets"].append(cat)
    return(len(cat))


def customer_can_afford_pet(customer, cat):
        if cat["price"] <= customer["cash"]:
            return(True)
        else:
            return(False)

