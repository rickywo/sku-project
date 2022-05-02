from unittest import TestCase
from src.Sku import Sku
from src.ProductManager import ProductManager


class TestProductManager(TestCase):
    pm = ProductManager()

    def test_product_manager_with_all_products_initially(self):
        self.assertIsNotNone(self.pm.get_product(Sku.MACBOOK_PRO))
        self.assertIsNotNone(self.pm.get_product(Sku.APPLE_TV))
        self.assertIsNotNone(self.pm.get_product(Sku.SUPER_IPAD))
        self.assertIsNotNone(self.pm.get_product(Sku.VGA_ADAPTER))

    def test_add_product_with_duplicate_sku_should_return_false(self):
        added = self.pm.add_product('ipd', 'Super iPad', 549.99)
        self.assertEqual(added, False)

    def test_add_product_without_duplicate_sku_should_return_true(self):
        added = self.pm.add_product('adr', 'Android', 466.99)
        self.assertEqual(added, True)

    def test_get_product_not_found_should_return_none(self):
        item = self.pm.get_product('nfd')
        self.assertEqual(item, None)

    def test_get_product_should_return_item_when_found(self):
        item = self.pm.get_product('ipd')
        self.assertEqual(item.get_sku(), 'ipd')
        self.assertEqual(item.get_name(), 'Super iPad')
        self.assertEqual(item.get_price(), 549.99)
