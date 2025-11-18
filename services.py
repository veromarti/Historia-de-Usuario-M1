import os
import files

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def add_product():
    print("\n\nEnter Product Information\n")
    name = input("Name -> ")
    #inventary["Product " + str(cont)]["Name"] = name.strip()
    pass

def show_inventory():
    inventory = files.load_file()
    print('\n')
    print(f'{"    Product    ":^18} {" Price ":^8} {"Quantity":^8}')
    print(f'{"---------------":<18} {"-------":^8} {"--------":^8}')
            
    for item in inventory:
        print(f"{item['name']:<18} | {item['price']:<8} | {item['quantity']:<8}")
    
    print(f'{"---------------":<18} {"-------":^8} {"--------":^}')

    print(input("\nPress enter to go back "))
    return  

def find_product():
    pass

def update_product():
    pass

def remove_product():
    pass

def total_units(inventory):
    units = 0
    units_list =[]
    for item in inventory:
        units += int(item['quantity'])
        units_list.append(int(item['quantity']))
    return units, units_list

def total_cost(inventory):#preguntar si es de todo el inventario o de cada producto
    total_cost = 0
    cost_list = []
    price_list = []
    for item in inventory:
        total_cost = int(item['quantity']) * float(item['price'])
        cost_list.append(total_cost)
        price_list.append(float(item['price']))
    return cost_list, price_list

def expensive_product(price_list):
    higher_price = max(price_list)
    position = price_list.index(higher_price)
    return position

def stats():
    inventory = files.load_file()
    stats_str = ["Total units: ", "Total cost: $", "Most expensive item:", "Item with largest stock"]
    t_units = total_units(inventory)
    t_cost, p_list = total_cost(inventory)
    pos_expensive = expensive_product(p_list)
    stats_values = [t_units]
    



    pass

def exit():
    pass
