"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2


# YOUR CODE STARTS HERE

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

if chosen_option == "1":
    print("Items in Warehouse 1: ", *warehouse1, sep="\n- ")
    print("")
    print("Items in Warehouse 2: ", *warehouse2, sep="\n- ")
    print("")
    print(f"Thank you for your visit, {username}!")

elif chosen_option == "2":
    search_query = input("What is the name of the item? name must be exact! ").lower()

    # search results will now be displayed in lower case :( not sure how to fix it
    warehouse1_lower = [item.lower() for item in warehouse1]
    warehouse2_lower = [item.lower() for item in warehouse2]

    total_count = warehouse1_lower.count(search_query) + warehouse2_lower.count(search_query)
    count_warehouse1 = warehouse1_lower.count(search_query)
    count_warehouse2 = warehouse2_lower.count(search_query)

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
        
            if order_query <= total_count:
                print(f"Your order of {order_query} {search_query}(s) has been placed!")
            
            elif order_query > total_count:
                print("Error, desired amount is higher than available stock!")
                out_of_stock_query = input(f"Would you like to order the maximum available stock of {total_count} {search_query}? (yes/no): ")
                
                if out_of_stock_query == "yes":
                    print(f"Your order of {total_count} {search_query}(s) has been placed!")
                else:
                    print(f"Thank you for your visit, {username}!")

        else:
            print(f"Thank you for your visit, {username}!")
    
    else:
        print(f"Thank you for your visit, {username}!")


elif chosen_option == "3":
    pass
else:
    print("Error, invalid entry. Please try again!")
    
    # input("Problem; please choose an option from the list by typing 1, 2 or 3 and push the enter key: ") 
    #need to make it loop. do I just give this a function and make it recursive?


# the items in the warehouse are written once or twice in order to simulate the amount of items the warehouse has in stock.