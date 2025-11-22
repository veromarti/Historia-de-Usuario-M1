import os
import files
import validation

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def add_product(inventory):
    print("- - - Adding product - - -\n")
    print("\nEnter Product Information\n")
    name = validation.str_entry()
    price = validation.float_entry("Price: ",0.001)
    quant = validation.int_entry("Quantity: ",1)
    product ={'name': name, 
              'price': price, 
              'quantity': quant}
    inventory.append(product)
    return inventory

def show_inventory(inventory):
    cont = 1
    print('\n')
    print(f'{" # ":^4} {"    Product    ":^18} {" Price ":^8} {"Quantity":^12}')
    print(f'{"---":<4} {"---------------":<18} {"-------":^8} {"--------":^12}')
            
    for item in inventory:
        print(f"{cont:^4} | {item['name'].capitalize():<18} | {item['price']:<10} | {item['quantity']:<14}")
        cont += 1
    print(f'{"---":<4} {"---------------":<18} {"-------":^8} {"--------":^12}')

    print(input("\nPress enter to go back "))
    return  

def find_product(product, inventory):
    product = product.lower()
    for item in inventory:
        if product in item['name'].lower():
            element = inventory.index(item)
            return item, element
    return None, None

def update_product(product, inventory, new_price = None, new_quant = None):
    print("- - - Updating product - - -\n")
    item, element = find_product(product, inventory)
    print(item)
    if new_price is not None:
        item['price'] = new_price
    if new_quant is not None:
        item['quantity'] = new_quant
    print("Product updated succesfully")
    return inventory    

def remove_product(product, inventory):
    print("- - - Removing product - - -\n")
    show_inventory(inventory)
    item, position = find_product(product, inventory)
    inventory.pop(position)
    print(inventory)
    return inventory    

def fusion(inventory,inventory_csv):
    final_inventory = inventory_csv
    for item in inventory:
        found_product, x = find_product(item['name'],inventory_csv)
        if found_product:
            found_product['price'] = item['price']
            found_product['quantity'] = item['quantity']
        else:
            final_inventory.append(item)
    return final_inventory
        
        

def exit():
    pass
