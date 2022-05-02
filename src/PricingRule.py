import math
from src.ProductManager import ProductManager
from src.Sku import Sku


# PricingRule
# Model class to hold Discount rule. This class should works as a model
class PricingRule:
    QUANTITY = 'num'
    PRICE = 'price'
    productManager = None
    __get_one_free_products = {Sku.APPLE_TV: {QUANTITY: 3}}
    __bulk_buy_products = {Sku.SUPER_IPAD: {QUANTITY: 4, PRICE: 499.99}}
    __bundle_buy_products = {Sku.VGA_ADAPTER: Sku.MACBOOK_PRO}

    def __init__(self, pm: ProductManager):
        self.productManager = pm

    # The discount rule should be applied when scanning an item
    # this function need to be able to calculate the subtotal
    # of a product and apply the discount rule to the price
    def apply_rule(self, sku, num_of_item, order):
        item = self.productManager.get_product(sku)
        if sku in self.__get_one_free_products:
            return self.get_one_free_handler(item, num_of_item)
        if sku in self.__bulk_buy_products:
            return self.bulk_buy_handler(item, num_of_item)
        if sku in self.__bundle_buy_products:
            return self.bundle_buy_handler(item, num_of_item, order)

        return num_of_item * item.get_price()

    def bulk_buy_handler(self, item, num_of_item):
        sku = item.get_sku()
        if num_of_item >= self.__bulk_buy_products[sku][self.QUANTITY]:
            return num_of_item * self.__bulk_buy_products[sku][self.PRICE]
        else:
            return num_of_item * item.get_price()

    def get_one_free_handler(self, item, num_of_item):
        sku = item.get_sku()
        price = item.get_price()
        # a complete set contains a free item
        set_price = price * (self.__get_one_free_products[sku][self.QUANTITY] - 1)
        num_of_set = math.floor(num_of_item / (self.__get_one_free_products[sku][self.QUANTITY]))

        if num_of_set < 1:
            return num_of_item * price
        else:
            sp = num_of_set * set_price  # multiply set_price to the number of set purchased
            # calculate the rest of item cannot form a set
            rs = num_of_item % self.__get_one_free_products[sku][self.QUANTITY]

            return sp + rs * price

    # Somehow I need the number of item of another bundle product from the order
    # items: the order structure from Checkout class
    def bundle_buy_handler(self, item, num_of_item, items):
        sku = item.get_sku()
        price = item.get_price()
        bundle_product = self.__bundle_buy_products[sku]

        if bundle_product in items:
            num_of_bundle_product = items[bundle_product]
            # deduct the amount of money based on the number of bundle product from the order
            # Example: 2 vga, 1 mbp. This function reduces charge to 2 vga to 1 because there is 1 mbp in the same order
            excessive_num_of_item = num_of_item - num_of_bundle_product['quantity']
            return (0, excessive_num_of_item * price)[excessive_num_of_item > 0]
        else:
            return num_of_item * price