import csv

def load_file():
    inventory_list = []
    with open("inventory.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:#intentar try
            inventory_list.append(row)
        return inventory_list

# def save_file():
#     with open("inventory.csv", "w") as file:
#         writer = csv.writer(file)