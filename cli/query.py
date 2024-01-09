from data import stock

# Get the user name
username = input("What is your user name? ")

# Greet the user
print(f"Hello, {username}!")

# Show the menu and ask to pick a choice
print("What would you like to do?")

options = ["1. List items by warehouse", "2. Search an item and place an order", "3. Quit"]
for option in options:
    print(option)

chosen_option = input("Type the number of the option you'd like to choose: ")


def clean_wh1_stock():
    warehouse1_items_list = []
    for item in stock:
        if item["warehouse"] == 1:
            warehouse1_items_list.append(item)
    return warehouse1_items_list


def print_wh1_stock():
    warehouse1_items_list = clean_wh1_stock()
    for item in warehouse1_items_list:
        print("- " + item["state"] + " " + item["category"])


def clean_wh2_stock():
    warehouse2_items_list = []
    for item in stock:
        if item["warehouse"] == 2:
            warehouse2_items_list.append(item)
    return warehouse2_items_list


def print_wh2_stock():
    warehouse2_items_list = clean_wh2_stock()
    for item in warehouse2_items_list:
        print("- " + item["state"] + " " + item["category"])


def count_wh1_stock():
    wh1_items = clean_wh1_stock()
    warehouse1_count = len(wh1_items)
    return warehouse1_count


def count_wh2_stock():
    wh2_items = clean_wh2_stock()
    warehouse2_count = len(wh2_items)
    return warehouse2_count


def count_total_stock():
    total_count_stock = count_wh1_stock() + count_wh2_stock()
    return total_count_stock


if chosen_option == "1":  # option 1
    print("Items in Warehouse 1: ")
    print_wh1_stock()
    print(" ")
    print("Items in Warehouse 2: ")
    print_wh2_stock()
    print(" ")
    print(f"Total items in Warehouse 1: {count_wh1_stock()}")
    print(" ")
    print(f"Total items in Warehouse 2: {count_wh2_stock()}")
    print(" ")
    print(f"Thank you for your visit, {username}!")


elif chosen_option == "2":  # option 2
    search_query = input("What is the name of the item you want to search for? ").lower()

    warehouse1_items = clean_wh1_stock()
    warehouse2_items = clean_wh2_stock()

    total_count = warehouse1_items.count(search_query) + warehouse2_items.count(search_query)
    count_warehouse1 = warehouse1_items.count(search_query)
    count_warehouse2 = warehouse2_items.count(search_query)

    if count_warehouse1 > 0 or count_warehouse2 > 0:
        print(f"Warehouse 1 has {count_warehouse1} {search_query}(s), Warehouse 2 has {count_warehouse2} {search_query}(s). Total: {total_count}")
    else:
        print("Not in stock.")

    if count_warehouse1 > count_warehouse2:
        print(f"Warehouse 1 has the highest amount of {search_query}(s): {count_warehouse1}")
    elif count_warehouse2 > count_warehouse1:
        print(f"Warehouse 2 has the highest amount of {search_query}(s): {count_warehouse2}")
    else:
        print("Error, restart.")

    if total_count >= 1:
        interest_query = input("Would you like to place an order? (yes/no): ")

        if interest_query == "yes":
            order_query = int(input("How many would you like to order? "))
            out_of_stock_query = input(f"We have {total_count} {search_query}(s) in stock. Is that enough? (yes/no): ")

            if out_of_stock_query == "yes":
                print(f"Your order of {total_count} {search_query}(s) has been placed!")
            else:
                print(f"Thank you for your visit, {username}!")
        else:
            print(f"Thank you for your visit, {username}!")
    else:
        print(f"Thank you for your visit, {username}!")


elif chosen_option == "3":
    print(f"Thank you for your visit, {username}!")
else:
    print("Error, invalid entry. Please try again!")

    # input("Problem; please choose an option from the list by typing 1, 2 or 3 and push the enter key: ")
    # need to make it loop. do I just give this a function and make it recursive?


# the items in the warehouse are written once or twice in order to simulate the amount of items the warehouse has in stock.
