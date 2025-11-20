import services
import validation
import files
import stats

flag_menu = False
add = "y"
flag_stats = False
element = 0

def main():
    print("\n- - - - - - WELCOME TO THE INVENTORY SYSTEM - - - - - -\n")

    text_menu= (
        "1. Add Product\n"
        "2. Show Inventory\n"
        "3. Find Product\n"
        "4. Update Product\n"
        "5. Remove Product\n"
        "6. Stats\n"
        "7. Save CSV file\n"
        "8. Load CSV file\n"
        "9. Exit\n"
        "\nChoose an option (1-9): "
    )
    option = validation.int_entry(text_menu, 1, 9)

    flag_menu = True
    return flag_menu, option

while not flag_menu:
    inven=files.load_file()
    flag_menu, option = main()

    if option == 1:
        while add == "y":
            services.add_product(inven)

    elif option == 2:
        services.show_inventory(inven)
        services.clear()

    elif option == 3:
        product = validation.str_entry()
        print(services.find_product(product, inven))

    elif option == 4:
        product = validation.str_entry()
        n_price = validation.float_entry("New Price: ", 0.001)
        n_quant = validation.int_entry("New Quantity: ", 1)
        services.update_product(product, inven, n_price, n_quant)

    elif option == 5:
        product = validation.str_entry()
        services.remove_product(product, inven)
        pass

    elif option == 6:
        stats_flag = False
        t_units, t_cost, exp_product, large_stock = stats.stats(inven)
        print(t_units)
        print(t_cost), 
        print(exp_product)
        print(large_stock)
        
        while not stats_flag:
            stats_flag, option = stats.menu()

            match option:
                case 1:
                    print(input("Total Units in Inventory : " + str(t_units) + "\nPress enter to continue..."))
                case 2:
                    print('\n')
                    print(f'{"    Product    ":^18} {" Price ":^8} {"Quantity":^12} {"Total Cost":^14}')
                    print(f'{"---------------":<18} {"-------":^8} {"--------":^12} {"----------":^14}')
                            
                    for item in inven:
                        print(f"{item['name']:<18} | {item['price']:<8} | {item['quantity']:<12} | {t_cost[element]:<18}")
                        element += 1
                    
                    print(f'{"---------------":<18} {"-------":^8} {"--------":^12} {"----------":^14}')

                    print(input("\nPress enter to go back "))
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass

    elif option == 7:
        pass

    elif option == 8:
        inventory = files.load_file()
    
    elif option == 9:
        services.exit()

    else:
        flag_menu = False

if __name__ == "__main__":
    main()