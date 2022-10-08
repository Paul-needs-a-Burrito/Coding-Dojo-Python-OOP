class Product:
    def __init__(self, name, price, category):
        self.product_name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if(is_increased):
            self.price += (percent_change * self.price)
        if (not is_increased):
            self.price -= (percent_change * self.price)
        return self

    def print_info(self):
        print(f"Product Name: {self.product_name}, Price: ${self.price}, Category: {self.category}")
        return self
