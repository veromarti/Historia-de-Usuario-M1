import csv
import validation

def load_file(csv_file):
    """This function receives the route of the .csv file and then it tries
        to use the file_ok() function from the module validation, to open the
        .csv file in read mode, to search for  invalid header, wrong number 
        of columns and negative value. It also evaluates possible errors while 
        trying to open the file, on each exception the user is informed of the 
        error. The function returns the .csv file with the valid rows as a list 
        of dictionaries.
    """

    inventory_list = []
    products = 0

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

def save_file(inventory,csv_file):
    """This function receives the inventory and the route of the .csv file to 
        try to open the file in write mode. Then it iterates through the list
        to write into the csv file each row (product information). In case of
        any error while trying to open and write into the .csv file it warns the 
        user and aborts the operation. The function returns a boolean value.
    """

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