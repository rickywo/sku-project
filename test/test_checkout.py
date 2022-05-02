from unittest import TestCase
from src.Checkout import Checkout
from src.PricingRule import PricingRule
from src.ProductManager import ProductManager


class TestCheckout(TestCase):
    productManager = ProductManager()
    pricingRule = PricingRule(productManager)

    def test_scan_with_invalid_input(self):
        co = Checkout(self.pricingRule)
        # accept an invalid input type
        response = co.scan('p')
        self.assertIsNone(response, 'Handle invalid argument')

    def test_scan_with_valid_input(self):
        co = Checkout(self.pricingRule)
        # accept an invalid input type
        response = co.scan(self.productManager.get_product('atv'))
        self.assertEqual(response, ('atv', 1, 109.50))
        # accept an invalid input type
        response = co.scan(self.productManager.get_product('atv'))
        self.assertEqual(response, ('atv', 2, 219.00))

    def test_purchase_3atv_get_one_free(self):
        co = Checkout(self.pricingRule)
        co.scan(self.productManager.get_product('atv'))
        co.scan(self.productManager.get_product('atv'))
        co.scan(self.productManager.get_product('atv'))
        co.scan(self.productManager.get_product('vga'))
        self.assertEqual(co.total(), 249.00)

    def test_bulk_buy_discount_on_ipads(self):
        co = Checkout(self.pricingRule)
        co.scan(self.productManager.get_product('atv'))
        co.scan(self.productManager.get_product('ipd'))
        co.scan(self.productManager.get_product('ipd'))
        co.scan(self.productManager.get_product('atv'))
        co.scan(self.productManager.get_product('ipd'))
        co.scan(self.productManager.get_product('ipd'))
        co.scan(self.productManager.get_product('ipd'))
        self.assertEqual(co.total(), 2718.95)

    def test_bundle_discount_macbook_and_adapter(self):
        co = Checkout(self.pricingRule)
        co.scan(self.productManager.get_product('mbp'))
        co.scan(self.productManager.get_product('vga'))
        co.scan(self.productManager.get_product('ipd'))
        self.assertEqual(co.total(), 1949.98)
