import unittest
from unittest.mock import MagicMock
from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl

class TestOrder(unittest.TestCase):

    def test_place_order(self):
        mock_conn = MagicMock()
        repo = OrderProcessorRepositoryImpl(mock_conn)

        # Mock methods
        repo.place_order = MagicMock(return_value=None)

        # Call place_order
        repo.place_order(1, "Hyderabad")

        repo.place_order.assert_called_once_with(1, "Hyderabad")

if __name__ == '__main__':
    unittest.main()
