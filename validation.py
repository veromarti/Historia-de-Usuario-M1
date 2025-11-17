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
    