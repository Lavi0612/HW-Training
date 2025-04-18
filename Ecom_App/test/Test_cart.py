import unittest
from entity.Cart import Cart

class TestCart(unittest.TestCase):

    def test_add_to_cart(self):
        # Create a cart item with expected test values
        cart = Cart(None, 1001, 2001, 2)

        # Assert the values correctly
        self.assertEqual(cart.customer_id, 1001)
        self.assertEqual(cart.product_id, 2001)
        self.assertEqual(cart.quantity, 2)

if __name__ == '__main__':
    unittest.main()
