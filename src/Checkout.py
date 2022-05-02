from src.PricingRule import PricingRule
from src.Product import Product


# Checkout
# This class is the controller of this project. It provides methods such as scan and total
class Checkout:
    QUANTITY = 'quantity'
    SUBTOTAL = 'subtotal'
    __order = {}  # a structure for storing purchased items of the order

    # { 'atv': {'quantity': 0, 'subtotal': Decimal('100')}}

    def __init__(self, pricing_rule):
        if not isinstance(pricing_rule, PricingRule):
            # raise an exception when argument is not an instance of PricingRule
            raise TypeError
        self.__rule = pricing_rule  # instance of PricingRule class
        self.__order = {}  # a structure for storing purchased items of the order

    # scan
    # param: item is an instance of Product class
    # output: example: 'atv', 4, 1299.99
    def scan(self, item):
        sku = item.get_sku()
        num_of_item = 0
        subtotal = 0
        self.__order[sku][self.SUBTOTAL] = subtotal
        return sku, num_of_item, subtotal

    # scan
    # param:
    # output: 1299.99
    def total(self):
        total = 0
        return total
