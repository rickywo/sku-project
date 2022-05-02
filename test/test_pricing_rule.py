from unittest import TestCase
from src.Checkout import Checkout
from src.PricingRule import PricingRule
from src.Sku import Sku
from src.ProductManager import ProductManager


class TestProductManager(TestCase):
    pm = ProductManager()
    pricingRule = PricingRule(pm)

    def test_bulk_buy_with_discount(self):
        price_for_4_ipads = self.pricingRule.bulk_buy_handler(self.pm.get_product(Sku.SUPER_IPAD), 4)
        self.assertEqual(price_for_4_ipads, 499.99 * 4)
        price_for_5_ipads = self.pricingRule.bulk_buy_handler(self.pm.get_product(Sku.SUPER_IPAD), 5)
        self.assertEqual(price_for_5_ipads, 499.99 * 5)

    def test_bulk_buy_without_discount(self):
        price_for_3_ipads = self.pricingRule.bulk_buy_handler(self.pm.get_product(Sku.SUPER_IPAD), 3)
        self.assertEqual(price_for_3_ipads, 549.99 * 3)

    def test_get_one_free_with_discount(self):
        price_for_3_atv = self.pricingRule.get_one_free_handler(self.pm.get_product(Sku.APPLE_TV), 3)
        self.assertEqual(price_for_3_atv, 109.50 * 2)
        price_for_5_atv = self.pricingRule.get_one_free_handler(self.pm.get_product(Sku.APPLE_TV), 5)
        self.assertEqual(price_for_5_atv, 109.50 * 4)

    def test_get_one_free_without_discount(self):
        price_for_2_atv = self.pricingRule.get_one_free_handler(self.pm.get_product(Sku.APPLE_TV), 2)
        self.assertEqual(price_for_2_atv, 109.50 * 2)
        price_for_1_atv = self.pricingRule.get_one_free_handler(self.pm.get_product(Sku.APPLE_TV), 1)
        self.assertEqual(price_for_1_atv, 109.50 * 1)

    def test_bundle_buy(self):
        order = {Sku.VGA_ADAPTER: {Checkout.QUANTITY: 2}, Sku.MACBOOK_PRO: {Checkout.QUANTITY: 1}}
        subtotal = self.pricingRule.bundle_buy_handler(self.pm.get_product(Sku.VGA_ADAPTER), 2, order)
        self.assertEqual(subtotal, 30)

