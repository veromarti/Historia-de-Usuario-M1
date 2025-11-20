import services
import validation
import files
import stats

flag_menu = False
add = "y"

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
            services.add_product()

    elif option == 2:
        services.show_inventory()
        services.clear()

    elif option == 3:
        product = validation.str_entry()
        services.find_product(product, inven)

    elif option == 4:
        product = validation.str_entry()
        n_price = validation.float_entry("New Price: ", 0.001)
        n_quant = validation.int_entry("New Quantity: ", 1)
        services.update_product(product, inven, n_price, n_quant)

    elif option == 5:
        services.remove_product()
        pass

    elif option == 6:
        stats.stats(inven)
        pass

    elif option == 8:
        inventory = files.load_file()
    
    elif option == 9:
        services.exit()

    else:
        flag_menu = False
