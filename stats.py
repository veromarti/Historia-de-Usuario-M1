import validation

def invent_list(inventory):
    price_list = []
    quant_list =[]
    for item in inventory:
        quant_list.append(int(item['quantity']))
        price_list.append(float(item['price']))

    return price_list, quant_list

def total_units(quantity_list):
    units = 0
    for item in range(len(quantity_list)):
        units += quantity_list[item]
    return units

        
def total_cost(price_list,quant_list):
    total_cost = 0
    cost_list = []
    
    for item in range(len(price_list)):
        total_cost = price_list[item] * quant_list[item]
        cost_list.append(round(total_cost,2))
    return cost_list

def expensive_product(price_list, inventory):
    higher_price = max(price_list)
    position = price_list.index(higher_price)
    item_name = inventory[position]['name']
    item_price = inventory[position]['price']
    return (item_name,item_price)

def largest_stock(quant_list, inventory):
    large_stock = max(quant_list)
    position = quant_list.index(large_stock)
    item_name = inventory[position]['name']
    item_quant = inventory[position]['quantity']
    return (item_name,item_quant)

def stats(inventory):
    p_list , q_list = invent_list(inventory)
    t_units = total_units(q_list)
    t_cost = total_cost(p_list,q_list)
    exp_product = expensive_product(p_list, inventory)
    large_stock = largest_stock(q_list,inventory)
    return t_units, t_cost, exp_product, large_stock


def menu():
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