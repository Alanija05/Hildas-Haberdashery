# All products are listed below
stock_list = [
    ["Sewing thread", 1.20, 184],
    ["Zipper", 0.65, 97],
    ["Wooden buttons", 1.80, 142],
    ["Iron on interfacing", 2.50, 76],
    ["Bias binding", 1.10, 213],
    ["Hook-and-eye set", 0.90, 58],
    ["Seam ripper", 1.50, 34],
    ["Tailors chalk", 1.25, 89],
    ["Elastic", 0.75, 167],
    ["Thimble", 1, 121]
]

# Total stock price calculation
total_stock_price = 0

for item in stock_list:
    item_stock_price = item[1] * item[2]
    total_stock_price += item_stock_price


# Print total stock price
print("Total stock price = £", total_stock_price)
