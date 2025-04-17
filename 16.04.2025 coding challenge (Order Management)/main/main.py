import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dao')))

from dao.OrderProcessor import OrderProcessor
from entity.User import User
from entity.Electronics import Electronics
from entity.Clothing import Clothing

def main():
    processor = OrderProcessor()

    while True:
        print("\nMenu:")
        print("1. Create User")
        print("2. Create Product")
        print("3. Create Order")
        print("4. Cancel Order")
        print("5. Get All Products")
        print("6. Get Order by User")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            try:
                user_id = int(input("Enter User ID: "))
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                role = input("Enter Role (Admin/User): ")
                user = User(user_id, username, password, role)
                success = processor.create_user(user)
                if success:
                    print("✅ User created successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            try:
                product_id = int(input("Enter Product ID: "))
                name = input("Enter product name: ")
                desc = input("Enter description: ")
                price = float(input("Enter price: "))
                stock = int(input("Enter stock quantity: "))
                ptype = input("Enter type (Electronics/Clothing): ")

                if ptype.lower() == "electronics":
                    brand = input("Enter brand: ")
                    warranty = int(input("Enter warranty period (months): "))
                    product = Electronics(product_id, name, desc, price, stock, "Electronics", brand, warranty)
                elif ptype.lower() == "clothing":
                    size = input("Enter size: ")
                    color = input("Enter color: ")
                    product = Clothing(product_id, name, desc, price, stock, "Clothing", size, color)
                else:
                    print("Invalid product type!")
                    return

                admin_id = int(input("Enter Admin user ID: "))
                admin = processor.get_user_by_id(admin_id)

                if admin is None or admin.role.lower() != "admin":
                    print("Only admins can create products.")
                    return

                processor.create_product(admin, product)
                print(f"✅ Product '{name}' created successfully.")
            except Exception as e:
                print(f"Error while creating product: {e}")

        elif choice == '3':
            try:
                user_id = int(input("Enter User ID: "))
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                role = "User"
                user = User(user_id, username, password, role)

                num_items = int(input("How many products to order? "))
                products = []

                for i in range(num_items):
                    product_id = int(input(f"Enter Product ID #{i+1}: "))
                    product = Electronics(product_id, "", "", 0.0, 0, "Electronics", "", 0)  # Placeholder Electronics product
                    products.append(product)

                processor.create_order(user, products)
                print("✅ Order created successfully.")
            except Exception as e:
                print(f"Error: {e}")


        elif choice == '4':
            try:
                user_id = int(input("Enter User ID: "))
                order_id = int(input("Enter Order ID: "))
                processor.cancel_order(user_id, order_id)
                print("✅ Order cancelled successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            try:
                products = processor.get_all_products()
                for row in products:
                    print(row)
                print("✅ Successfully got all products.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '6':
            try:
                user_id = int(input("Enter User ID: "))
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                role = "User"
                user = User(user_id, username, password, role)

                orders = processor.get_order_by_user(user)
                for order in orders:
                    print(order)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
