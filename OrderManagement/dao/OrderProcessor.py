from util.DBConnUtil import get_db_connection
from exception.user_not_found_exception import UserNotFoundException
from exception.order_not_found_exception import OrderNotFoundException
from entity.User import User
from entity.Clothing import Clothing
from entity.Electronics import Electronics

class OrderProcessor:
    def __init__(self):
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

    def create_user(self, user):
        try:
            self.cursor.execute("""
                INSERT INTO Users (username, password, role)
                VALUES (?, ?, ?)
            """, (user.username, user.password, user.role))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False

    def create_product(self, user, product):
        if user.role != 'Admin':
            raise PermissionError("Only Admin can create products.")

        try:
            self.cursor.execute("""
            INSERT INTO Products (productName, description, price, quantityInStock, type)
            VALUES (?, ?, ?, ?, ?)
            """, (
                product.product_name,
                product.description,
                product.price,
                product.quantity_in_stock,
                product.type
            ))
            self.conn.commit()
        except Exception as e:
            print(f"Error creating product: {e}")
            raise

    def create_order(self, user, products):
        try:
            # Ensure user exists
            self.cursor.execute("SELECT * FROM Users WHERE id=?", (user.user_id,))
            if not self.cursor.fetchone():
                self.create_user(user)

            # Create order
            self.cursor.execute("INSERT INTO Orders (user_id) OUTPUT Inserted.id VALUES (?)", (user.user_id,))
            order_id = self.cursor.fetchone()[0]

            # Add order details
            for p in products:
                self.cursor.execute(
                    "INSERT INTO OrderDetails (order_id, product_id, quantity) VALUES (?, ?, ?)",
                    (order_id, p.product_id, 1)
                )
            self.conn.commit()
        except Exception as e:
            print(f"Error creating order: {e}")
            raise

    def cancel_order(self, user_id, order_id):
        try:
            self.cursor.execute("SELECT * FROM Orders WHERE order_id=? AND user_id=?", (order_id, user_id))
            if not self.cursor.fetchone():
                raise OrderNotFoundException("Order or User not found")
            self.cursor.execute("DELETE FROM Orders WHERE order_id=?", (order_id,))
            self.conn.commit()
        except Exception as e:
            print(f"Error cancelling order: {e}")
            raise

    def get_all_products(self):
        try:
            self.cursor.execute("SELECT * FROM Products")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching products: {e}")
            return []

    def get_order_by_user(self, user):
        try:
            self.cursor.execute("SELECT * FROM Orders WHERE user_id=?", (user.user_id,))
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching orders: {e}")
            return []

    def get_user_by_id(self, user_id):
        try:
            self.cursor.execute(
                "SELECT user_id, username, password, role FROM Users WHERE user_id=?",
                (user_id,)
            )
            row = self.cursor.fetchone()
            if row:
                return User(user_id=row[0], username=row[1], password=row[2], role=row[3])
            return None
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None
