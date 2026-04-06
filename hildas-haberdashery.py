from tkinter import * # type: ignore
import os

main_window = Tk()

def create_main_window():
    # Initialize Main Window
    global main_window
    main_window.title("Hilda's Haberdashery Program")

    main_window_label = Label(main_window,
                              text="Welcome to Hilda's Haberdashery Program",
                              font=("Calibri", 30))
    main_window_label.grid(row=0, column=0, columnspan=2)

    display_all_items_button = Button(main_window,
                                      text="Display all items",
                                      font=("Calibri",15),
                                      command=display_all_items)
    display_all_items_button.grid(row=1, column=0, padx=15, pady=15)

    display_single_item_button = Button(main_window,
                                      text="Display single item",
                                      font=("Calibri",15),
                                      command=display_single_item)
    display_single_item_button.grid(row=2, column=0, padx=15, pady=15)

    add_item_button = Button(main_window,
                                      text="Add item",
                                      font=("Calibri",15),
                                      command=add_item)
    add_item_button.grid(row=1, column=1, padx=15, pady=15)

    remove_item_button = Button(main_window,
                                      text="Remove item",
                                      font=("Calibri",15),
                                      command=remove_item)
    remove_item_button.grid(row=2, column=1, padx=15, pady=15)

    change_stock_button = Button(main_window,
                                      text="Change stock",
                                      font=("Calibri",15),
                                      command=change_stock)
    change_stock_button.grid(row=3, column=0, padx=15, pady=15)

    change_price_button = Button(main_window,
                                      text="Change price",
                                      font=("Calibri",15),
                                      command=change_price)
    change_price_button.grid(row=3, column=1, padx=15, pady=15)

    quick_info_button = Button(main_window,
                                      text="Quick info",
                                      font=("Calibri",15),
                                      command=quick_info)
    quick_info_button.grid(row=4, column=0, padx=15, pady=15)

    exit_system_button = Button(main_window,
                                      text="Exit system",
                                      font=("Calibri",15),
                                      command=exit_system)
    exit_system_button.grid(row=4, column=1, padx=15, pady=15)

class gb_button(Button):
    def __init__(self, child_window, parent_window):
        super().__init__(
            child_window,
            text = "Go back",
            font = ("Calibri",15),
            command = lambda: go_back(child_window, parent_window)
        )
        self.grid(row=15, column=0, columnspan=2, padx=15, pady=15)

def go_back(child, parent):
    child.destroy()
    parent.deiconify()



def display_all_items():
    main_window.withdraw()
    display_all_items_window = Toplevel(main_window)

    try:
        with open("products.csv", "r") as file:
            main_label = Label(display_all_items_window,
                               text="Displaying all products",
                               font=("Calibri", 15))
            main_label.grid(row=0, column=0, columnspan=2)

            for i, line in enumerate(file):
                split_line = line.split(",")
                product_label = Label(display_all_items_window,
                                      text=f" - Product: {split_line[0]}   |   Price: {split_line[1]}   |   Stock level: {split_line[2]}",
                                        font=("Calibri", 15))
                product_label.grid(row=i + 1, column=0, columnspan=2, pady=15)

    except Exception as ex:
        print(f"Data not read - {ex}")

    go_back_button = gb_button(display_all_items_window, main_window)

    


def display_single_item():
    main_window.withdraw()
    display_single_item_window = Toplevel(main_window)
    display_single_item_window.geometry("600x400")

    main_label = Label(display_single_item_window,
                    text="Search for item to display data",
                    font=("Calibri", 30))
    main_label.grid(row=0, column=0, columnspan=2)

    error_label = Label(display_single_item_window,
                        font=("Calibri", 15))
                
    product_label = Label(display_single_item_window,
                          font=("Calibri", 15))

    def find_and_display_item(item_name):
        try:
            with open("products.csv", "r") as file:
                found = False
                
                for i, line in enumerate(file):
                    split_line = line.split(",")

                    if split_line[0] == item_name.lower():
                        found = True

                        product_label.config(text=f" - Product: {split_line[0]}   |   Price: {split_line[1]}   |   Stock level: {split_line[2]}")    
                        product_label.grid(row=i + 4, column=0, columnspan=2, pady=15)
                        break

                if found:
                    error_label.config(text=" ")
                
                else:
                    error_label.config(text="Product not found")

                error_label.grid(row=3, column=0, columnspan=2)

        except Exception as ex:
            print(f"Data not read - {ex}")

    product_entry = Entry(display_single_item_window)
    product_entry.grid(row=1, column=0, columnspan=2, pady=15)

    product_entry_submit = Button(display_single_item_window,
                                  text="Search for item",
                                  font=("Calibri", 15),
                                  command=lambda: find_and_display_item(str(product_entry.get())))
    product_entry_submit.grid(row=2, column=0, columnspan=2, pady=15)



    go_back_button = gb_button(display_single_item_window, main_window)



def add_item():
    main_window.withdraw()
    add_item_window = Toplevel(main_window)
    add_item_window.geometry("300x350")

    error_label = Label(add_item_window,
                        font=("Calibri", 15))

    def write_item_to_file(item_name: str, price: float, stock: int):
        try:
            with open("products.csv", "a") as file:
                line = f"{item_name},{price},{stock}"
                file.write(line)
                
        except Exception as ex:
            print(f"Data not read - {ex}")

    item_name_label = Label(add_item_window,
                            text="Name:",
                            font=("Calibri", 15))
    item_name_label.grid(row=1, column=0, pady=15)

    item_name_entry = Entry(add_item_window)
    item_name_entry.grid(row=1, column=1, pady=15)


    price_label = Label(add_item_window,
                            text="Price:",
                            font=("Calibri", 15))
    price_label.grid(row=2, column=0, pady=15)

    price_entry = Entry(add_item_window)
    price_entry.grid(row=2, column=1, pady=15)


    stock_label = Label(add_item_window,
                            text="Stock:",
                            font=("Calibri", 15))
    stock_label.grid(row=3, column=0, pady=15)

    stock_entry = Entry(add_item_window)
    stock_entry.grid(row=3, column=1, pady=15)


    def validate_and_add_item():
        item_name = item_name_entry.get().strip()
        price = price_entry.get().strip()
        stock = stock_entry.get().strip()

        if not item_name or not price or not stock:
            error_label.config(text="All fields must be filled in")
            error_label.grid(row=6, column=0, columnspan=2, pady=15)
            return

        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            error_label.config(text="Price must be a number, stock must be a whole number")
            error_label.grid(row=6, column=0, columnspan=2, pady=15)
            return

        write_item_to_file(item_name, price, stock)


    product_entry_submit = Button(add_item_window,
                                  text="Add item",
                                  font=("Calibri", 15),
                                  command=validate_and_add_item)
    product_entry_submit.grid(row=4, column=0, columnspan=2, pady=15)

    go_back_button = gb_button(add_item_window, main_window)



def remove_item():
    main_window.withdraw()
    remove_item_window = Toplevel(main_window)
    remove_item_window.geometry("300x300")

    message_label = Label(remove_item_window,
                          font=("Calibri", 15))

    def find_and_remove(item_name):
        try:
            found = False
            with open("products.csv", "r") as infile, open(".products_temp.csv", "w") as outfile:
                for line in infile:
                    split_line = line.split(',')
                    
                    if not item_name.lower() == split_line[0]:
                        outfile.write(line)

                    else:
                        found = True
                
                os.replace(".products_temp.csv", "products.csv")

                if found:
                    message_label.config(text="Item found and deleted")
                    
                else:
                    message_label.config(text="Item not found")

                message_label.grid(row=2, column=0, columnspan=2, pady=15)
                    

        except Exception as ex:
            print(f"Data not read - {ex}")

    item_name_label = Label(remove_item_window,
                            text="Name:",
                            font=("Calibri", 15))
    item_name_label.grid(row=0, column=0, pady=15)

    item_name_entry = Entry(remove_item_window)
    item_name_entry.grid(row=0, column=1, pady=15)

    item_name_submit = Button(remove_item_window,
                                  text="Remove item",
                                  font=("Calibri", 15),
                                  command=lambda: find_and_remove(str(item_name_entry.get())))
    item_name_submit.grid(row=1, column=0, columnspan=2, pady=15)

    go_back_button = gb_button(remove_item_window, main_window)



def change_stock():
    main_window.withdraw()
    change_stock_window = Toplevel(main_window)
    change_stock_window.geometry("500x330")

    message_label = Label(change_stock_window,
                          font=("Calibri", 15))

    def find_and_change_stock(item_name: str, target_stock: str):
        try:
            found = False
            with open("products.csv", "r") as infile, open(".products_temp.csv", "w") as outfile:
                for line in infile:
                    split_line = line.split(',')
                    
                    if not item_name.lower() == split_line[0]:
                        outfile.write(line)

                    else:
                        line = f"{split_line[0]},{split_line[1]},{target_stock}\n"
                        outfile.write(line)
                        found = True
                
                os.replace(".products_temp.csv", "products.csv")

                if found:
                    message_label.config(text=f"Item {item_name} found and stock chaged  to {target_stock}")
                    
                else:
                    message_label.config(text=f"Item {item_name} not found")

                message_label.grid(row=3, column=0, columnspan=2, pady=15, padx=15)
                    

        except Exception as ex:
            print(f"Data not read - {ex}")

    item_name_label = Label(change_stock_window,
                            text="Name:",
                            font=("Calibri", 15))
    item_name_label.grid(row=0, column=0, pady=15)

    item_name_entry = Entry(change_stock_window)
    item_name_entry.grid(row=0, column=1, pady=15)

    target_stock_label = Label(change_stock_window,
                            text="Stock:",
                            font=("Calibri", 15))
    target_stock_label.grid(row=1, column=0, pady=15)

    target_stock_entry = Entry(change_stock_window)
    target_stock_entry.grid(row=1, column=1, pady=15)

    change_stock_submit = Button(change_stock_window,
                                  text="Change stock",
                                  font=("Calibri", 15),
                                  command=lambda: find_and_change_stock(str(item_name_entry.get()), 
                                                                        str(target_stock_entry.get())))
    change_stock_submit.grid(row=2, column=0, columnspan=2, pady=15)

    go_back_button = gb_button(change_stock_window, main_window)



def change_price():
    main_window.withdraw()
    change_price_window = Toplevel(main_window)
    change_price_window.geometry("300x300")

    message_label = Label(change_price_window,
                          font=("Calibri", 15))

    def find_and_change_price(item_name: str, target_price: str):
        try:
            found = False
            with open("products.csv", "r") as infile, open(".products_temp.csv", "w") as outfile:
                for line in infile:
                    split_line = line.split(',')
                    
                    if not item_name.lower() == split_line[0]:
                        outfile.write(line)

                    else:
                        line = f"{split_line[0]},{target_price},{split_line[2]}\n"
                        outfile.write(line)
                        found = True
                
                os.replace(".products_temp.csv", "products.csv")

                if found:
                    message_label.config(text=f"Item {item_name} found and price chaged  to {target_price}")
                    
                else:
                    message_label.config(text=f"Item {item_name} not found")

                message_label.grid(row=3, column=0, columnspan=2, pady=15, padx=15)
                    

        except Exception as ex:
            print(f"Data not read - {ex}")

    item_name_label = Label(change_price_window,
                            text="Name:",
                            font=("Calibri", 15))
    item_name_label.grid(row=0, column=0, pady=15)

    item_name_entry = Entry(change_price_window)
    item_name_entry.grid(row=0, column=1, pady=15)

    target_price_label = Label(change_price_window,
                            text="Stock:",
                            font=("Calibri", 15))
    target_price_label.grid(row=1, column=0, pady=15)

    target_price_entry = Entry(change_price_window)
    target_price_entry.grid(row=1, column=1, pady=15)

    change_price_submit = Button(change_price_window,
                                  text="Change price",
                                  font=("Calibri", 15),
                                  command=lambda: find_and_change_price(str(item_name_entry.get()), 
                                                                        str(target_price_entry.get())))
    change_price_submit.grid(row=2, column=0, columnspan=2, pady=15)

    go_back_button = gb_button(change_price_window, main_window)



def quick_info():
    main_window.withdraw()
    quick_info_window = Toplevel(main_window)
    quick_info_window.geometry("270x250")

    total_stock_price_label = Label(quick_info_window,
                                    font=("Calibri", 15))
    
    total_stock_quantity_label = Label(quick_info_window,
                                       font=("Calibri", 15))
    
    try:
        with open("products.csv", "r") as file:
            total_stock_price = 0
            total_stock_quantity = 0

            for line in file:
                split_line = line.split(',')

                total_stock_price += float(split_line[1]) * int(split_line[2])
                total_stock_quantity += int(split_line[2])

            total_stock_price_label.config(text=f"Total stock price: {round(total_stock_price, 2)}")
            total_stock_price_label.grid(row=0, column=0, columnspan=2, padx=15, pady=15)

            total_stock_quantity_label.config(text=f"Total stock quantity: {total_stock_quantity}")
            total_stock_quantity_label.grid(row=1, column=0, columnspan=2, padx=15, pady=15)
            
    except Exception as ex:
        print(f"Data not read - {ex}")

    go_back_button = gb_button(quick_info_window, main_window)



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



def calculate_total_stock_price_from_file(filename: str) -> float:
    total_stock_price = 0

    with open(filename, "r") as file:
        for line in file:
            split_line = line.split(",")
            total_stock_price += (float(split_line[1]) * int(split_line[2]))

    return total_stock_price



def add_stock_to_file(item_name: str, filename: str, increase_amount=1) -> None:
    product_found = False

    try:
        with open(filename, "r") as infile, open(".products_temp.csv", "w") as outfile:
            for line in infile:
                split_line = line.split(",")

                if item_name.lower() == split_line[0]:
                    split_line[2] = str(int(split_line[2]) + increase_amount)
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



def remove_stock_from_file(item_name: str, filename: str, decrease_amount=1) -> None:
    product_found = False
    try:
        with open(filename, "r") as infile, open(".products_temp.csv", "w") as outfile:
            for line in infile:
                split_line = line.split(",")

                if item_name.lower() == split_line[0]:
                    split_line[2] = str(int(split_line[2]) - decrease_amount)
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

            print(f"\nStock successfully updated for {item_name} by -{decrease_amount} for a total of {new_stock_level}")

    except Exception as ex:
        print(f"Data not updated - {ex}")



def manually_change_stock_in_file(item_name: str, filename: str, change_amount: int) -> None:
    product_found = False
    try:
        with open(filename, "r") as infile, open(".products_temp.csv", "w") as outfile:
            for line in infile:
                split_line = line.split(",")

                if item_name.lower() == split_line[0]:
                    split_line[2] = str(change_amount)
                    line = split_line[0] + "," + str(split_line[1]) + "," + str(split_line[2]) + "\n"
                    product_found = True

                outfile.write(line)

            if product_found == False:
                print("\nProduct not found")
                return
        
        with open(filename, "w") as infile, open(".products_temp.csv", "r") as outfile:
            for line in outfile:
                infile.write(line)

            print(f"\nStock successfully changed for {item_name} to {change_amount}")
            
    except Exception as ex:
        print(f"Data not updated - {ex}")

def exit_system():
    global main_window
    main_window.destroy()



def main():
    create_main_window()
    main_window.mainloop()
    exit_system = False

    """
    print("Welcome to Hilda's Haberdashery system! What would you like to do:")
    while exit_system == False:
        print("\n0. Display stock list\n1. Print item details\n2. Calculate total stock price\n3. Add stock\n4. Remove stock\n5. Manually change stock\n6. Exit system")
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
                    try:
                        print_item_from_file(item_name=input("\nEnter item name: "), filename="products.csv")
                    except Exception as ex:
                        print(f"Exception caught - {ex}")

                case "2":
                    total_stock_price = calculate_total_stock_price_from_file("products.csv")
                    print(f"\nThe total stock price is £{total_stock_price:.2f}")

                case "3":
                    try:
                        add_stock_to_file(item_name=input("\nEnter item name: "), filename="products.csv", increase_amount=int(input("\nEnter increase amount: ")))
                    except ValueError as e:
                        print(f"\nException caught - {e}\nMake sure to enter the correct data type")

                case "4":
                    try:
                        remove_stock_from_file(item_name=input("\nEnter item name: "), filename="products.csv", decrease_amount=int(input("\nEnter decrease amount: ")))
                    except ValueError as e:
                        print(f"\nException caught - {e}\nMake sure to enter the correct data type")

                case "5":
                    try:
                        manually_change_stock_in_file(item_name=input("\nEnter item name: "), filename="products.csv", change_amount=int(input("\nEnter change amount: ")))
                    except ValueError as e:
                        print(f"\nException caught - {e}\nMake sure to enter the correct data type")

                case "6":
                    exit_system = True

                case _:
                    print("\nOption not recognized, try again!")
    """

main()