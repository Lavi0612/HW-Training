from abc import ABC, abstractmethod
from entity.Customer import Customer
from entity.Product import Product
from entity.Cart import Cart


class OrderProcessorRepository(ABC):

    @abstractmethod
    def add_customer(self, customer: Customer):
        """Add a new customer to the database."""
        pass

    @abstractmethod
    def add_product(self, product: Product):
        """Add a new product to the database."""
        pass

    @abstractmethod
    def add_to_cart(self, cart: Cart):
        """Add a product to the customer's cart."""
        pass

    @abstractmethod
    def place_order(self, customer_id: int, shipping_address: str):
        """Place an order for the customer based on their cart items."""
        pass

    @abstractmethod
    def view_customers(self):
        """Retrieve and display all customers."""
        pass

    @abstractmethod
    def view_products(self):
        """Retrieve and display all products."""
        pass

    @abstractmethod
    def view_cart_items(self, customer_id: int):
        """Retrieve and display all items in a customer's cart."""
        pass

    @abstractmethod
    def view_orders(self):
        """Retrieve and display all orders."""
        pass

    @abstractmethod
    def delete_customer(self, customer_id: int):
        """Delete a customer by ID."""
        pass

    @abstractmethod
    def delete_product(self, product_id: int):
        """Delete a product by ID."""
        pass

    @abstractmethod
    def remove_from_cart(self, customer_id: int, product_id: int):
        """Remove a product from a customer's cart."""
        pass

    @abstractmethod
    def view_orders_by_customer(self, customer_id: int):
        """Retrieve and display all orders for a specific customer."""
        pass

    @abstractmethod
    def remove_order(self, order_id: int):
        """Remove an order by ID."""
        pass
