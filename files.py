import csv
import validation

def load_file():
    inventory_list = []
    products = 0
    
    csv_file = "inventory.csv"

    try:
        file_ok, inventory_list, = validation.file_ok(csv_file)
        if file_ok:
            print ("CSV file loaded succesfully")
            print(inventory_list)
            # with open("inventory.csv","r") as file:
            #     reader = csv.DictReader(file)
            #     for row in reader:
            #         row['price'] = float(row['price'])
            #         row['quantity'] = int(row['quantity'])
            #         inventory_list.append(row)
                
            #     print ("CSV file loaded succesfully")
            #     return inventory_list
        else:
            pass
    
    except UnicodeDecodeError:
        print("Wrong file encoding")
        return inventory_list, 0, 0
    
    except FileNotFoundError:
        print(f"File not found {csv_file}")
        return inventory_list, 0, 0
    
    except Exception as error:
        print(f"Unexpected error: {error}")
        return inventory_list, 0, 0

# def save_file():
#     with open("inventory.csv", "w") as file:
#         writer = csv.writer(file)