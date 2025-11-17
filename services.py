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

def stats():
    inventory = files.load_file()
    
    pass

def exit():
    pass
