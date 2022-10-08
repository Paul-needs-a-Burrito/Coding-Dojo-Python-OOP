# Assignment: Store & Products
# Objectives:
#    Practice creating classes
#    Practice associations between classes
#    Practice modularizing code
# Start by creating a Store class that has 2 attributes: a name and a list of products. The name must be provided upon creation, but the products list should be empty.
# Next, create a Product class that has 3 attributes: a name, a price, and a category. All of these should be provided upon creation.
# 1) Create a Store class with 2 attributes
# 2) Create a Product class with 3 attributes
# 3) Add print_info(self) to the Product class - print the name of the product, its category, and its price.
# 4) Add update_price(self, percent_change, is_increased) to the Product class - updates the product's price. If is_increased is True, the price should increase by the percent_change provided. If False, the price should decrease by the percent_change provided.
# 5) Add add_product(self, new_product) to the Store class - takes a product and adds it to the store
# 6) Add sell_product(self, id) to the Store class - remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.
# 7) Test out your classes by creating an instance of the Store and a few instances of the Product class, add those instances to the store instance, and then test out the methods.
# 8) NINJA BONUS: Add inflation(self, percent_increase) to the Store class - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
# 9) NINJA BONUS: Add set_clearance(self, category, percent_discount) to the Store class - updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)
# 10) NINJA BONUS: Modularize your code into 3 separate files
# 11) SENSEI BONUS: Update the product class to give each product a unique id. Update the sell_product method to accept the unique id.


class Store:
    def __init__(self, name):
        self.store_name = name
        self.products_list = []

    def add_product(self, new_product):
        self.products_list.append(new_product)
        return self

    def sell_product(self, id):
        self.products_list.pop(id)
        return self

    def inflation(self, percent_increase):
        for i in range(len(self.products_list)):
            self.products_list[i].update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for i in range(len(self.products_list)):
            self.products_list[i]['category'].update_price(percent_discount, False)
        return self

# NOTE: I WAS UNABLE TO COMPLETE #9 SO AS TO ONLY AFFECT A SPECIFIC CATEGORY. I SKIPPED #11 BECAUSE ASSIGNMENT WAS TAKING TOO LONG