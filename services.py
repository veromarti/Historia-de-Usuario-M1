import os
import files
import validation

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def add_product(inventory):
    print("\n\nEnter Product Information\n")
    name = validation.str_entry()
    price = validation.float_entry("Price: ",0.001)
    quant = validation.int_entry("Quantity: ",1)
    product ={'name': name, 
              'price': price, 
              'quantity': quant}
    inventory.append(product)
    return

def show_inventory(inventory):
    print('\n')
    print(f'{"    Product    ":^18} {" Price ":^8} {"Quantity":^8}')
    print(f'{"---------------":<18} {"-------":^8} {"--------":^8}')
            
    for item in inventory:
        print(f"{item['name']:<18} | {item['price']:<8} | {item['quantity']:<8}")
    
    print(f'{"---------------":<18} {"-------":^8} {"--------":^}')

    print(input("\nPress enter to go back "))
    return  

def find_product(product, inventory):
    product = product.lower()
    for item in inventory:
        if product in item['name'].lower():
            element = inventory.index(item)
            return item, element
    return None

def update_product(product, inventory, new_price = None, new_quant = None):
    item = find_product(product, inventory)
    if new_price is not None:
        item['price'] = new_price
    if new_quant is not None:
        item['quantity'] = new_quant
    return inventory    

def remove_product(product, inventory):
    item, position = find_product(product, inventory)
    inventory.pop(position)
    return inventory    

def exit():
    pass
