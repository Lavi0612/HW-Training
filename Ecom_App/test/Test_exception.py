import unittest
from exception.CustomerNotFoundException import CustomerNotFoundException
from exception.ProductNotFoundException import ProductNotFoundException

class TestException(unittest.TestCase):

    def test_customer_not_found_exception(self):
        with self.assertRaises(CustomerNotFoundException):
            raise CustomerNotFoundException("Customer Not Found")

    def test_product_not_found_exception(self):
        with self.assertRaises(ProductNotFoundException):
            raise ProductNotFoundException("Product Not Found")

if __name__ == '__main__':
    unittest.main()
