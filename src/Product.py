class Product:
    __sku = ''
    __name = ''
    __price = 0

    def __init__(self, sku, name, price):
        self.__sku = sku
        self.__name = name
        self.__price = price

    def get_sku(self):
        return self.__sku

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price