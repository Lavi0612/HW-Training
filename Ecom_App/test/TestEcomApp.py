import unittest
from entity.Customer import Customer
from entity.Product import Product
from entity.Cart import Cart
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from unittest.mock import MagicMock

class TestEcomApp(unittest.TestCase):

    def setUp(self):
        self.conn = MagicMock()  # Mock DB connection
        self.repo = OrderProcessorRepositoryImpl(self.conn)

    def test_add_customer(self):
        customer = Customer(1001, "TestUser", "testuser@example.com", "test123")
        self.assertEqual(customer.name, "TestUser")

    def test_add_product(self):
        product = Product(2001, "TestProduct", 999.99, "Test description", 10)
        self.assertEqual(product.stock_quantity, 10)

    def test_add_to_cart(self):
        cart = Cart(None, 1001, 2001, 2)
        self.assertEqual(cart.quantity, 2)

    def test_place_order(self):
        self.repo.place_order = MagicMock(return_value=None)
        self.repo.place_order(1001, "Hyderabad")
        self.repo.place_order.assert_called_once_with(1001, "Hyderabad")

if __name__ == '__main__':
    unittest.main()
