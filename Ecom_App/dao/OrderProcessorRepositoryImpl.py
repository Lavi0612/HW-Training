import pyodbc
import datetime
from dao.OrderProcessorRepository import OrderProcessorRepository
from exception.CustomerNotFoundException import CustomerNotFoundException
from exception.ProductNotFoundException import ProductNotFoundException
from exception.OrderNotFoundException import OrderNotFoundException


class OrderProcessorRepositoryImpl(OrderProcessorRepository):

    def __init__(self, conn):
        self.conn = conn

    def add_customer(self, customer):
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO customers (customer_id, name, email, password)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (customer.customer_id, customer.name, customer.email, customer.password))
            self.conn.commit()
            print("Customer added successfully!")
        except Exception as e:
            print("Error while adding customer:", e)

    def add_product(self, product):
        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO products (product_id, name, price, description, stockQuantity) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (product.product_id, product.name, product.price, product.description, product.stock_quantity))
            self.conn.commit()
            print("Product added successfully!")
        except Exception as e:
            print("Error while adding product:", e)

    def add_to_cart(self, cart):
        try:
            cursor = self.conn.cursor()

            # Check if customer exists
            cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (cart.customer_id,))
            if not cursor.fetchone():
                raise CustomerNotFoundException(f"Customer with ID {cart.customer_id} not found.")

            # Check if product exists
            cursor.execute("SELECT * FROM products WHERE product_id = ?", (cart.product_id,))
            if not cursor.fetchone():
                raise ProductNotFoundException(f"Product with ID {cart.product_id} not found.")

            query = """
                INSERT INTO cart (customer_id, product_id, quantity)
                VALUES (?, ?, ?)
            """
            cursor.execute(query, (cart.customer_id, cart.product_id, cart.quantity))
            self.conn.commit()
            print("Product added to cart successfully.")
        except Exception as e:
            print("Error adding product to cart:", e)

    def place_order(self, customer_id, shipping_address):
        try:
            cursor = self.conn.cursor()

            # Check if customer exists
            cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
            if not cursor.fetchone():
                raise CustomerNotFoundException(f"Customer with ID {customer_id} not found.")

            # Retrieve cart items
            cursor.execute("SELECT product_id, quantity FROM cart WHERE customer_id = ?", (customer_id,))
            cart_items = cursor.fetchall()

            if not cart_items:
                print("No items in cart to place an order.")
                return

            total_amount = 0

            for product_id, quantity in cart_items:
                cursor.execute("SELECT price FROM products WHERE product_id = ?", (product_id,))
                product = cursor.fetchone()
                if product:
                    total_amount += product[0] * quantity
                else:
                    raise ProductNotFoundException(f"Product with ID {product_id} not found.")

            order_date = datetime.datetime.now()

            cursor.execute("""
                INSERT INTO orders (customer_id, order_date, total_amount, shipping_address)
                VALUES (?, ?, ?, ?)
            """, (customer_id, order_date, total_amount, shipping_address))
            self.conn.commit()

            print(f"Order placed successfully! Total Amount: {total_amount}")

            cursor.execute("DELETE FROM cart WHERE customer_id = ?", (customer_id,))
            self.conn.commit()

        except Exception as e:
            print("Error placing order:", e)

    def view_customers(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM customers")
        for row in cursor.fetchall():
            print(row)

    def view_products(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        for row in cursor.fetchall():
            print(row)

    def view_cart_items(self, customer_id):
        cursor = self.conn.cursor()

        # Check if customer exists
        cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
        if not cursor.fetchone():
            raise CustomerNotFoundException(f"Customer with ID {customer_id} not found.")

        cursor.execute("SELECT * FROM cart WHERE customer_id = ?", (customer_id,))
        items = cursor.fetchall()
        if not items:
            print("Cart is empty.")
        else:
            for row in items:
                print(row)

    def view_orders(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM orders")
        for row in cursor.fetchall():
            print(row)

    def delete_customer(self, customer_id):
        cursor = self.conn.cursor()

        # Check if customer exists
        cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
        if not cursor.fetchone():
            raise CustomerNotFoundException(f"Customer with ID {customer_id} not found.")

        cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))
        self.conn.commit()
        print(f"Customer with ID {customer_id} deleted successfully.")

    def delete_product(self, product_id):
        cursor = self.conn.cursor()

        # Check if product exists
        cursor.execute("SELECT * FROM products WHERE product_id = ?", (product_id,))
        if not cursor.fetchone():
            raise ProductNotFoundException(f"Product with ID {product_id} not found.")

        cursor.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
        self.conn.commit()
        print(f"Product with ID {product_id} deleted successfully.")

    def remove_from_cart(self, customer_id, product_id):
        cursor = self.conn.cursor()

        # Check if customer exists
        cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
        if not cursor.fetchone():
            raise CustomerNotFoundException(f"Customer with ID {customer_id} not found.")

        # Check if product exists
        cursor.execute("SELECT * FROM products WHERE product_id = ?", (product_id,))
        if not cursor.fetchone():
            raise ProductNotFoundException(f"Product with ID {product_id} not found.")

        cursor.execute("DELETE FROM cart WHERE customer_id = ? AND product_id = ?", (customer_id, product_id))
        self.conn.commit()
        print(f"Product with ID {product_id} removed from cart for customer ID {customer_id}.")

    def view_orders_by_customer(self, customer_id):
        cursor = self.conn.cursor()

        # Check if customer exists
        cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
        if not cursor.fetchone():
            raise CustomerNotFoundException(f"Customer with ID {customer_id} not found.")

        cursor.execute("SELECT * FROM orders WHERE customer_id = ?", (customer_id,))
        orders = cursor.fetchall()

        if not orders:
            raise OrderNotFoundException(f"No orders found for customer ID {customer_id}.")
        else:
            print(f"Orders for Customer ID {customer_id}:")
            for order in orders:
                print(order)
    def remove_order(self, order_id):
        try:
            cursor = self.conn.cursor()

        # Check if order exists
            cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
            if not cursor.fetchone():
                raise OrderNotFoundException(f"Order with ID {order_id} not found.")

        # First delete from order_items
            cursor.execute("DELETE FROM order_items WHERE order_id = ?", (order_id,))
        
        # Then delete from orders
            cursor.execute("DELETE FROM orders WHERE order_id = ?", (order_id,))

            self.conn.commit()
            print(f"Order with ID {order_id} removed successfully.")

        except Exception as e:
            print("Error while deleting order:", e)



