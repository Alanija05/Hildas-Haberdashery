# All products are listed below
stock_list = [
    ["sewing thread", 1.20, 184],
    ["zipper", 0.65, 97],
    ["wooden buttons", 1.80, 142],
    ["iron on interfacing", 2.50, 76],
    ["bias binding", 1.10, 213],
    ["hook-and-eye set", 0.90, 58],
    ["seam ripper", 1.50, 34],
    ["tailors chalk", 1.25, 89],
    ["elastic", 0.75, 167],
    ["thimble", 1, 121]
]

def add_stock(item_name: str, increase_amount=1) -> None:
    for item in stock_list:
        if item_name.lower() == item[0]:
            item[2] += increase_amount
            print(f"\nItem found. Increased stock by {increase_amount} for a total of {item[2]}")
            return
    print("Item not found")


exit_system = False

print("Welcome to Hilda's Haberdashery system! What would you like to do:")
while exit_system == False:
    print("\n1. Print total stock price\n2. Print item stock\n3. Print item price\n4. Add stock\n5. Quit")
    try:
        choice = input("\nEnter what you would like to do (1-4): ")

        match choice:
            case "1":
                # Total stock price calculation
                total_stock_price = 0

                for item in stock_list:
                    item_stock_price = item[1] * item[2]
                    total_stock_price += item_stock_price

                # Print total stock price
                print("Total stock price = £", total_stock_price)

            case "2":
                item_found = False
                item_name = input("\nEnter the name of the item: ")
                for item in stock_list:
                    if item_name.lower() == item[0]:
                        item_found = True
                        print(f"\nThe stock of {item[0]} is {item[2]}")

                if item_found == False:
                    print("Item not found")

            case "3":
                item_found = False
                item_name = input("\nEnter the name of the item: ")
                for item in stock_list:
                    if item_name.lower() == item[0]:
                        item_found = True
                        print(f"\nThe stock of {item[0]} is {item[2]}")

                if item_found == False:
                    print("Item not found")

            case "4":
                try:
                    item_name = input("\nEnter the name of the item: ")
                    increase_amount = int(input("\nEnter the number to increase the stock by: "))
                    add_stock(item_name=item_name, increase_amount=increase_amount)
                except ValueError as e:
                    print(f"\nException caught - {e}\nMake sure to enter the correct data type")

            case "5":
                exit_system = True

            case _:
                print("\nOption not recognized, try again!")
    except Exception as e:
        print(f"\nUnknow exception caught - {e}")
        exit_system = True