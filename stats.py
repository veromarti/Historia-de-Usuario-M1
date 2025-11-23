import validation

def invent_list(inventory):
    """This function receives a list of dictionaries and returns
        2 lists, one for the column of the prices and the other
        for the column of the quantities
    """

    price_list = []
    quant_list =[]
    for item in inventory:
        quant_list.append(int(item['quantity']))
        price_list.append(float(item['price']))

    return price_list, quant_list

def total_units(quantity_list):
    """This function receives list with the products quantities
        and returns the sum of all the elements in the list
    """

    units = 0
    for item in range(len(quantity_list)):
        units += quantity_list[item]
    return units

        
def total_cost(price_list,quant_list):
    """This function receives the lists of the quantities and
        the prices, and returns the resulted list of the 
        operation price_list[postion] * quant_list[postion]
    """

    total_cost = 0
    cost_list = []
    
    for item in range(len(price_list)):
        total_cost = price_list[item] * quant_list[item]
        cost_list.append(round(total_cost,2))
    return cost_list

def expensive_product(price_list, inventory):
    """This function receives the list of the prices and the
        inventory, it finds the maximum value inside the list, then
        it obtains the [position] of the maximum value with which it
        searches inside the list of dictionaries (inventory) the product
        in the [position]. The function returns the name and the price of 
        the most expensive product 
    """

    higher_price = max(price_list)
    position = price_list.index(higher_price)
    item_name = inventory[position]['name']
    item_price = inventory[position]['price']
    return (item_name,item_price)

def largest_stock(quant_list, inventory):
    """This function receives the list with the quantities and the
        inventory, it finds the maximum value inside the list, then
        it obtains the [position] of the maximum value with which it
        searches inside the list of dictionaries (inventory) the product
        in the [position]. The function returns the name and the quantity of 
        product with the largest stock 
    """

    large_stock = max(quant_list)
    position = quant_list.index(large_stock)
    item_name = inventory[position]['name']
    item_quant = inventory[position]['quantity']
    return (item_name,item_quant)

def stats(inventory):
    """This function receives the inventory, and it returns the sum of all the 
        products, the list of total costs, the most expensive product with its
        price, and the product with largest stock with its quantity 
    """

    p_list , q_list = invent_list(inventory)
    t_units = total_units(q_list)
    t_cost = total_cost(p_list,q_list)
    exp_product = expensive_product(p_list, inventory)
    large_stock = largest_stock(q_list,inventory)
    return t_units, t_cost, exp_product, large_stock


def menu():
    """This function shows the statistics menu, validates the option entered 
        by the user and returns a boolean value with the option chosen
    """

    print("\n- - - - STATISTICS - - - -\n")
    text_menu= (
        "1. Total Units\n"
        "2. Total Cost\n"
        "3. Most Expensive Item\n"
        "4. Item with Largest Stock\n"
        "5. Back\n"
        "\nChoose an option (1-5): "
    )
    option = validation.int_entry(text_menu, 1, 5)
    flag = False
    return flag, option