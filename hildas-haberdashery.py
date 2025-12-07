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


# Function to initialize the file. Not used in working program
def write_to_file(dataset: list, filename: str) -> None:
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



def display_all_items_from_file(filename: str) -> None:
    try:
        with open(filename, "r") as file:
            print("\nDisplaying all products\n")
            for line in file:
                split_line = line.split(",")
                print(f" - Product: {split_line[0]}   |   Price: {split_line[1]}   |   Stock level: {split_line[2]}")
    except Exception as ex:
        print(f"Data not read - {ex}")

    

def print_item_from_file(item_name: str, filename: str) -> None:
    try:
        with open(filename, "r") as file:
            for line in file:
                split_line = line.split(",")
                if item_name.lower() == split_line[0]:
                    print("\nFound product. Displaying details:\n")
                    print(f" - Product: {split_line[0]}   |   Price: {split_line[1]}   |   Stock level: {split_line[2]}")
                    return
            print("\nProduct not found")
    except Exception as ex:
        print(f"Data not read - {ex}")



def add_stock_to_file(item_name: str, filename: str, increase_amount=1) -> None:
    product_found = False
    try:
        with open(filename, "r") as infile, open(".products_temp.csv", "w") as outfile:
            for line in infile:
                split_line = line.split(",")
                if item_name.lower() == split_line[0]:
                    split_line[2] = int(split_line[2]) + increase_amount
                    line = split_line[0] + "," + str(split_line[1]) + "," + str(split_line[2]) + "\n"
                    new_stock_level = split_line[2]
                    product_found = True
                outfile.write(line)
            if product_found == False:
                print("\nProduct not found")
                return
        
        with open(filename, "w") as infile, open(".products_temp.csv", "r") as outfile:
            for line in outfile:
                infile.write(line)
            print(f"\nStock successfully updated for {item_name} by {increase_amount} for a total of {new_stock_level}")
    except Exception as ex:
        print(f"Data not updated - {ex}")



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




def main():
    exit_system = False

    print("Welcome to Hilda's Haberdashery system! What would you like to do:")
    while exit_system == False:
        print("\n0. Display stock list\n1. Print item details\n2. Calculate total stock price\n3. Add stock\n4. Remove stock\n5. Exit system")
        try:
            choice = input("\nEnter what you would like to do (0-5): ")

        except Exception as e:
            print(f"\nUnknow exception caught - {e}")
            exit_system = True
        
        else:
            match choice:
                case "0":
                    display_all_items_from_file("products.csv")

                case "1":
                    try:
                        print_item_from_file(item_name=input("\nEnter item name: "), filename="products.csv")
                    except Exception as ex:
                        print(f"Exception caught - {ex}")

                case "2":
                    total_stock_price = calculate_total_stock_price()
                    print(f"\nThe total stock price is £{total_stock_price:.2f}")

                case "3":
                    try:
                        add_stock_to_file(item_name=input("Enter item name: "), filename="products.csv", increase_amount=int(input("Enter increase amount: ")))
                    except ValueError as e:
                        print(f"\nException caught - {e}\nMake sure to enter the correct data type")

                case "4":
                    try:
                        remove_stock(item_name=input("\nEnter the name of the item: "), decrease_amount=int(input("\nEnter the number to decrease the stock by: ")))
                    except ValueError as e:
                        print(f"\nException caught - {e}\nMake sure to enter the correct data type")

                case "5":
                    exit_system = True

                case _:
                    print("\nOption not recognized, try again!")

main()