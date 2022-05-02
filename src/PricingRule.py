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
        """ Virtually private constructor. """
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
        return 0

    # Somehow I need the number of item of another bundle product from the order
    # items: the order structure from Checkout class
    def bundle_buy_handler(self, item, num_of_item, items):
        return 0