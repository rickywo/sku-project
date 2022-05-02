from src.Product import Product


class ProductManager:
    __products = {}

    def __seed_products(self):
        # SKU	Name	Price
        # ipd	Super iPad	$549.99
        # mbp	MacBook Pro	$1399.99
        # atv	Apple TV	$109.50
        # vga	VGA adapter	$30.00
        self.add_product('ipd', 'Super iPad', 549.99)
        self.add_product('mbp', 'MacBook Pro', 1399.99)
        self.add_product('atv', 'Apple TV', 109.50)
        self.add_product('vga', 'VGA adapter', 30.00)

    def __init__(self):
        self.__seed_products()

    def add_product(self, sku, name, price):
        if sku in self.__products:
            return False
        else:
            self.__products[sku] = Product(sku, name, price)
            return True

    def get_product(self, sku):
        if sku in self.__products:
            return self.__products[sku]
        else:
            return None
