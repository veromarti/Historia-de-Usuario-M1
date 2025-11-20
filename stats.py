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
        cost_list.append(total_cost)
    return cost_list

def expensive_product(price_list, inventory):
    higher_price = max(price_list)
    position = price_list.index(higher_price)
    item_name = inventory[position]['name']
    item_price = inventory[position]['price']
    return (item_name,item_price)

def stats(inventory):
    #inventory = files.load_file()
    stats_str = ["Total units: ", "Total cost: $", "Most expensive item:", "Item with largest stock"]
    p_list , q_list = invent_list(inventory)
    t_units = total_units(q_list)
    t_cost = total_cost(p_list,q_list)
    exp_product = expensive_product(p_list, inventory)
    stats_values = [t_units]
    # print(p_list)
    # print(q_list)
    # print(t_units)
    # print(t_cost)
    print(exp_product[0])
    print(exp_product[1])