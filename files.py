import csv
import validation

def load_file():
    inventory_list = []
    products = 0
    csv_file = input('Enter the file name (inventory.csv): ').strip()

    try:
        file_ok, inventory_list, rows, products = validation.file_ok(csv_file)
        if file_ok:
            print ("\nCSV file loaded succesfully\n")
            print ("Invalid rows found: " + str(rows) +"\n")
            print ("Loaded products: " + str(products) +"\n")
        else:
            print ("CSV file could not be loaded")
    
    except UnicodeDecodeError:
        print("Wrong file encoding")
    
    except FileNotFoundError:
        print(f"File not found {csv_file}")
    
    except Exception as error:
        print(f"Unexpected error: {error}")
    
    return inventory_list

def save_file(inventory):

    csv_file = input('Enter the file name (inventory.csv): ').strip()

    try:
        with open(csv_file, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            writer.writerow(['name','price','quantity'])

            for item in inventory:
                writer.writerow([item["name"], item["price"], item["quantity"]])
        
        print("Inventory saved as "+ csv_file)
        return True
    
    except Exception as error:
        print(f"Unexpected error: {error}")
        return False