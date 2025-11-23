import os
import validation

def clear():
    """This function uses the 'os' module to detect the operative
        system of the computer. In case of windows it sets the command
        'cls' and for unix devices it sets the command 'clear' to erase 
        the console 
    """

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def add_product(inventory):
    """This function receives the list of dictionaries, it asks for
        the new product information to the user, each field is validated
        accordingly, then it adds the new product to the end of the list,
        and it returns the inventory with the new prduct
    """

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
    """This function receives the list of dictionaries and it shows
        each element like an organized kind of table
    """

    cont = 1
    print('\n')
    print(f'{" # ":^4} {"    Product    ":^18} {" Price ":^8} {"Quantity":^12}')
    print(f'{"---":<4} {"---------------":<18} {"-------":^8} {"--------":^12}')
            
    for item in inventory:
        print(f"{cont:^4} | {item['name'].capitalize():<18} | {item['price']:<10} | {item['quantity']:<14}")
        cont += 1
    print(f'{"---":<4} {"---------------":<18} {"-------":^8} {"--------":^12}')

    return  

def find_product(product, inventory):
    """This function receives the name of the product to be found and the
        inventory, it iterates through the list,and if it finds the product 
        in the inventory it returns its information and index in the list.
        If the product is not found it returns None, None
    """
        
    product = product.lower()
    for item in inventory:
        if product in item['name'].lower():
            element = inventory.index(item)
            return item, element
    return None, None

def update_product(product, inventory, new_price = None, new_quant = None):
    """This function receives the name of the product to be updated,the
        inventory, the new price and new quantity it uses the find_product()
        function to obtain the product information, then it overwrites the
        price and quantity values. It returns the updated inventory
    """

    item, element = find_product(product, inventory)
    if item is not None:
        if new_price is not None:
            item['price'] = new_price
        if new_quant is not None:
            item['quantity'] = new_quant
        print("\nProduct updated succesfully")
    else:print("\nNo product found\n")
    return inventory    

def remove_product(product, inventory):
    """This function receives the name of the product to be removed and the
        inventory, it uses the find_product() function to obtain the product 
        position inside the inventory list, then it removes the product using .pop()
        It returns the updated inventory
    """

    print("- - - Removing product - - -")
    show_inventory(inventory)
    item, position = find_product(product, inventory)
    if position is not None:
        inventory.pop(position)
        print("Product removed successfully")
        show_inventory(inventory)
    else:print("No product found\n")
    return inventory    

def fusion(inventory,inventory_csv):
    """This function receives the inventory created by the user in the
        program and the .csv file loaded from the project folder. It updates
        the product information if it exists in both inventories. The function
        returns the fused inventory.
    """

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
