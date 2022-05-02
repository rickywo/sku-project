from src.Product import Product


class ProductManager:
    __products = {}

    def __seed_products(self):
        # SKU	Name	Price
        # ipd	Super iPad	$549.99
        # mbp	MacBook Pro	$1399.99
        # atv	Apple TV	$109.50
        # vga	VGA adapter	$30.00
        return

    def __init__(self):
        """ Virtually private constructor. """
        self.__seed_products()

    def add_product(self, sku, name, price):
        return False

    def get_product(self, sku):
        return None