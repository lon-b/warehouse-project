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
    search_query = input("What is the name of the item? name must be exact! ")
    total_count = warehouse1.count(search_query) + warehouse2.count(search_query)
    count_warehouse1 = warehouse1.count(search_query)
    count_warehouse2 = warehouse2.count(search_query)

    if count_warehouse1 > 0 or count_warehouse2 > 0:
        print(f"Warehouse 1 has {count_warehouse1} {search_query}(s), Warehouse 2 has {count_warehouse2} {search_query}(s). Total: {total_count}")
    else:
        print("Not in stock.")
elif chosen_option == "3":
    print("chose 3")
else:
    input("Problem; please choose an option from the list by typing 1, 2 or 3 and push the enter key: ") 
    #need to make it loop. do I just give this a function and make it recursive?


# the items in the warehouse are written once or twice in order to simulate the amount of items the warehouse has in stock.

# If they pick 1
#
# Else, if they pick 2
#
# Else, if they pick 3
#
# Else

# Thank the user for the visit

