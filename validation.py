def int_entry(message, min=None, max=None):
    flag = False
    while not flag:
        try:
            value = int(input(message).strip())
            if min is not None and value < min or max is not None and value > max:
                raise ValueError
            return value
        except ValueError:
            print("Wrong Entry. Try again: ")

def float_entry(message,min=None):
    flag = False
    while not flag:
        try:
            value = float(input(message).strip())
            if min is not None and value < min:
                raise ValueError
            return value
        except ValueError:
            print("Wrong Entry. Try again: ")

def str_entry():
    flag = False
    while not flag:
        item_name = input("Name: ").strip()
        if not item_name:
            print("The name cannot be empty \n")
            continue
        if not all(c.isalnum() or c.isspace() for c in item_name):
            print("The name must include only letters or numbers\n")
            continue
        break
    return item_name

def yes_no(decision):
    flag = False
    while not flag:
        if not decision:
            print("Choose an option \n")
            continue
        if not all(c.isalpha() for c in decision):
            print("Invalid option. Try Again\n")
            continue
        break
    return decision.lower()

def file_ok(csv_file):
    import csv
    header = ['name','price','quantity']
    invalid_rows = 0
    inventory = []
    products = 0
    
    with open(csv_file, newline = "", encoding = "utf-8") as file:
        reader = csv.reader(file)
        is_file_ok = True

        try:
            current_header = next(reader)

            if current_header != header:
                print("Wrong CSV header")
                is_file_ok = False
                return is_file_ok, inventory, products
            
            # if columns != 3:
            #     print("Header is invalid. The header must contain exactly 3 columns")
            #     is_file_ok = False
            #     invalid_rows += 1
            #     return is_file_ok, inventory

            for num, row in enumerate(reader, start=2):
                if len(row) != 3:
                    print("Row #" + str(num) + " is invalid. Ommited row")
                    invalid_rows += 1
                    continue

                name, price, quantity = row

                try:
                    price = float(price)
                    quantity = int(quantity)

                    if price <= 0 or quantity<= 0:
                        raise ValueError
            
                except ValueError:
                    print("Row #" + str(num) + " is invalid. Ommited row due to price/quantity cannot be a negative value")
                    invalid_rows += 1
                    continue

                inventory.append({
                    'name':name,
                    'price':float(price),
                    'quantity':int(quantity)
                })

                products += 1
        
        except StopIteration:
            print("CSV file cannot not be empy")
            is_file_ok = False

    return is_file_ok, inventory, invalid_rows, products

        
        
