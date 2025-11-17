import csv



def load_file():
    inventory_list = []
    with open("inventory.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            #print(row)
            inventory_list.append(row)
        #print(inventory_list)
        return inventory_list


#load_file()

# def save_file():
#     with open("inventory.csv", "w") as file:
#         writer = csv.writer(file)