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



def write_to_file(dataset: list, filename: str):
    try:
        file = open(filename, "w+")
    except Exception as ex:
        print(f"Data not written - {ex}")
    else:
        file.write("Product name, Price, Stock\n")
        for item in dataset:
            line = item[0] + ",£" + str(item[1]) + "," + str(item[2]) + "\n"
            file.write(line)
        print(f"Data written to {filename}")
    finally:
        file.close()



def display_all_items_from_file(filename):
    try:
        with open(filename, "r") as file:
            print("\nDisplaying all products\n")
            for line in file:
                split_line = line.split(",")
                print(f" - Product: {split_line[0]}   |   Price: {split_line[1]}   |   Stock level: {split_line[2]}")
    except Exception as ex:
        print(f"Data not read - {ex}")
        
    


def add_stock(item_name: str, increase_amount=1) -> None:
    for item in stock_list:
        if item_name.lower() == item[0]:
            item[2] += increase_amount
            print(f"\nItem found. Increased stock by {increase_amount} for a total of {item[2]}")
            return
    print("Item not found")



def remove_stock(item_name: str, decrease_amount=1) -> None:
    for item in stock_list:
        if item_name.lower() == item[0]:
            item[2] -= decrease_amount
            print(f"\nItem found. Decreased stock by {decrease_amount} for a total of {item[2]}")
            return
    print("Item not found")



def calculate_total_stock_price() -> float:
    total_stock_price = 0

    for item in stock_list:
        item_stock_price = item[1] * item[2]
        total_stock_price += item_stock_price

    return total_stock_price



def print_item_price(item_name: str) -> None:
    for item in stock_list:
        if item_name.lower() == item[0]:
            print(f"\nThe price of {item[0]} is £{item[1]:.2f}")
            return
    print("Item not found")



def print_item_stock(item_name: str) -> None:
    for item in stock_list:
        if item_name.lower() == item[0]:
            print(f"\nThe stock of {item[0]} is {item[2]}")
            return
    print("Item not found")



def main():
    exit_system = False

    print("Welcome to Hilda's Haberdashery system! What would you like to do:")
    while exit_system == False:
        print("\n0. Display stock list\n1. Print total stock price\n2. Print item stock\n3. Print item price\n4. Add stock\n5. Remove stock\n6. Exit system")
        try:
            choice = input("\nEnter what you would like to do (0-6): ")

        except Exception as e:
            print(f"\nUnknow exception caught - {e}")
            exit_system = True
        
        else:
            match choice:
                case "0":
                    display_all_items_from_file("products.csv")

                case "1":
                    total_stock_price = calculate_total_stock_price()
                    print(f"\nThe total stock price is £{total_stock_price:.2f}")

                case "2":
                    print_item_stock(item_name=input("\nEnter the name of the item: "))

                case "3":
                    print_item_price(item_name=input("\nEnter the name of the item: "))

                case "4":
                    try:
                        add_stock(item_name=input("\nEnter the name of the item: "), increase_amount=int(input("\nEnter the number to increase the stock by: ")))
                    except ValueError as e:
                        print(f"\nException caught - {e}\nMake sure to enter the correct data type")

                case "5":
                    try:
                        remove_stock(item_name=input("\nEnter the name of the item: "), decrease_amount=int(input("\nEnter the number to decrease the stock by: ")))
                    except ValueError as e:
                        print(f"\nException caught - {e}\nMake sure to enter the correct data type")

                case "6":
                    exit_system = True

                case _:
                    print("\nOption not recognized, try again!")

main()