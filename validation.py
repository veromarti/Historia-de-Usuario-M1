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