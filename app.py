import services
import validation
import files
import stats

flag_menu = False

flag_stats = False
element = 0

def main():
    print("\n- - - - - - WELCOME TO THE INVENTORY SYSTEM - - - - - -\n")

    text_menu= (
        "1. Add Products\n"
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

    return option

inven = files.load_file()
while not flag_menu:
    
    option = main()

    if option == 1:
        add = "y"
        while add == "y":
            inven = services.add_product(inven)

            add = validation.yes_no(input("\nAdd another product (y/n) -> "))

            # if add == "y":
            #     pass
            # if add == "n":
                # a
            

    elif option == 2:
        services.show_inventory(inven)
        services.clear()

    elif option == 3:
        product = validation.str_entry()
        print(services.find_product(product, inven))#poner que muestre bonito y solo info[0]

    elif option == 4:
        product = validation.str_entry()
        n_price = validation.float_entry("New Price: ", 0.001)
        n_quant = validation.int_entry("New Quantity: ", 1)
        services.update_product(product, inven, n_price, n_quant)

    elif option == 5:
        product = validation.str_entry()
        services.remove_product(product, inven)

    elif option == 6:
        stats_flag = False
        t_units, t_cost, exp_product, large_stock = stats.stats(inven)
        
        while not stats_flag:
            stats_flag, option = stats.menu()
            element = 0

            match option:
                case 1:
                    print("- - - Total Units in Inventory - - -\n")
                    print(input("Total Quantity : " + str(t_units) + "\n\nPress enter to go back..."))

                case 2:
                    print("- - - - Inventory with Total Cost per Product - - - -\n")
                    print(f'{" # ":^4} {"    Product    ":^18} {" Price ":^8} {"Quantity":^12} {"Total Cost":^14}')
                    print(f'{"---":<4} {"---------------":<18} {"-------":^8} {"--------":^12} {"----------":^14}')
                            
                    for item in inven:
                        print(f"{(element+1):^4} | {item['name'].capitalize():<18} | {item['price']:<8} | {item['quantity']:<12} | {t_cost[element]:<18}")
                        element += 1
                    
                    print(f'{"---":<4} {"---------------":<18} {"-------":^8} {"--------":^12} {"----------":^14}')
                    print(input("\nPress enter to go back... "))

                case 3:
                    print("- - - Most Expensive Product - - -\n")
                    print("Item: " + exp_product[0].capitalize() + " - Price: $" + str(exp_product[1]))
                    print(input("\nPress enter to go back..."))
                    
                case 4:
                    print("- - - Product with Largest Stock - - -\n")
                    print("Item: " + large_stock[0].capitalize() + " - Quantity: " + str(large_stock[1]))
                    print(input("\nPress enter to go back..."))

                case 5:
                    stats_flag = True
                    flag_menu = False

    elif option == 7:
        pass

    elif option == 8:
        inven=files.load_file()
    
    elif option == 9:
        flag_menu = True
        print("\n Thanks for using the Inventory System")
        services.exit()

    else:
        flag_menu = False

if __name__ == "__main__":
    main()