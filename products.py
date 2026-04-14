class Product:

    def __init__(self, p_id, name, cost, sales, stock, status):
        self._id = p_id
        self._product_name = name
        self._cost_price = cost
        self._sales_price = sales
        self._current_stock = stock
        self._discontinued = 1 if status else 0

    def get_id(self):
        return self._id

    def get_product_name(self):
        return self._product_name

    def set_product_name(self, new_name):
        self._product_name = new_name

    def get_cost_price(self):
        return self._cost_price

    def set_cost_price(self, new_price):
        self._cost_price = new_price

    def get_sales_price(self):
        return self._sales_price

    def set_sales_price(self, new_price):
        self._sales_price = new_price

    def get_current_stock(self):
        return self._current_stock

    def set_stock(self, amount):
        self._current_stock = amount

    def get_product_information(self):
        return self._product_name + ": " \
                    + str(self._current_stock) + " pieces available, cost price: " \
                    + str(self._cost_price) + ", sales price: " \
                    + str(self._sales_price)

