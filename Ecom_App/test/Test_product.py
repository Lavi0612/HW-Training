import unittest
from entity.Product import Product

class TestProduct(unittest.TestCase):

    def test_product_creation(self):
        product = Product(1, "Laptop", 50000, "Gaming Laptop", 10)
        self.assertEqual(product.product_id, 1)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 50000)
        self.assertEqual(product.description, "Gaming Laptop")
        self.assertEqual(product.stock_quantity, 10)

if __name__ == '__main__':
    unittest.main()
