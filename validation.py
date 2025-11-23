def int_entry(message, min=None, max=None):
    """This function validates that entry typed by the user 
        is an int value, if the value is inside range (min-max)
        and it is an int number the function returns the value
    """

    flag = False
    while not flag:
        try:
            value = int(input(message).strip())
            if min is not None and value < min or max is not None and value > max:
                raise ValueError
            return value
        except ValueError:
            print("\nWrong Entry. Try again\n")

def float_entry(message,min=None):
    """This function validates that entry typed by the user 
        is a float value, if the value is bigger than min value
        and it is a float number the function returns the value
    """

    flag = False
    while not flag:
        try:
            value = float(input(message).strip())
            if min is not None and value < min:
                raise ValueError
            return value
        except ValueError:
            print("\nWrong Entry. Try again\n")

def str_entry():
    """This function validates that entry typed by the user 
        is a string, if the entry is composed by alphanumeric
        characters and/or spaces it returns the string
    """

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
    """This function validates that entry typed by the user 
        is a 'y' or a 'n', if yes the function returns the 
        decision variable
    """

    flag = False
    while not flag:
        if not decision:
            print("\nChoose an option \n")
            return
        if not all(decision.lower()=="y" or decision.lower()=="n" or c.isdigit() for c in decision):
            print("\nInvalid option. Try Again\n")
            return
        break
    return decision.lower()

def file_ok(csv_file):
    """This function validates that the .csv file has the correct
        header, that every row has exactly 3 columns, and that
        values in the price and quantity columns are bigger than 0.
        In case of any of the above it will show an error to the user,
        and it will ommit invalid rows. The function returns a boolean,
        the .csv file content save in a list of dictionaries, the number
        of invalid rows, and the amount of correct rows found (products loaded)
    """

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
                return is_file_ok, inventory, invalid_rows, products
            

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
