from src.PricingRule import PricingRule
from Checkout import Checkout
from src.ProductManager import ProductManager

if __name__ == '__main__':
    productManager = ProductManager()
    co = Checkout(PricingRule(productManager))
    co.scan(productManager.get_product('mbp'))
    co.scan(productManager.get_product('vga'))
    co.scan(productManager.get_product('vga'))
    print(co.total())
