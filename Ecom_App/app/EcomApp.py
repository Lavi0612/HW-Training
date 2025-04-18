from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from util.DBConnUtil import DBConnUtil
from entity.Customer import Customer
from entity.Product import Product
from entity.Cart import Cart
from exception.CustomerNotFoundException import CustomerNotFoundException
from exception.ProductNotFoundException import ProductNotFoundException
from exception.OrderNotFoundException import OrderNotFoundException


def main():
    conn = DBConnUtil.get_db_connection()
    repo = OrderProcessorRepositoryImpl(conn)

    while True:
        try:
            print("\n===== E-Commerce Application =====")
            print("1. Add Customer")
            print("2. Add Product")
            print("3. Add To Cart")
            print("4. Place Order")
            print("5. View Customers")
            print("6. View Products")
            print("7. View Cart Items")
            print("8. View All Orders")
            print("9. Delete Customer")
            print("10. Delete Product")
            print("11. Remove From Cart")
            print("12. View Orders By Customer")
            print("13. Remove Order")           
            print("14. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                customer_id = int(input("Enter Customer ID: "))
                name = input("Enter Customer Name: ")
                email = input("Enter Customer Email: ")
                password = input("Enter Customer Password: ")
                customer = Customer(customer_id, name, email, password)
                repo.add_customer(customer)

            elif choice == 2:
                product_id = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                price = float(input("Enter Product Price: "))
                description = input("Enter Product Description: ")
                stock_quantity = int(input("Enter Product Stock Quantity: "))
                product = Product(product_id, name, price, description, stock_quantity)
                repo.add_product(product)

            elif choice == 3:
                customer_id = int(input("Enter Customer ID: "))
                product_id = int(input("Enter Product ID: "))
                quantity = int(input("Enter Quantity: "))
                cart = Cart(None, customer_id, product_id, quantity)
                repo.add_to_cart(cart)

            elif choice == 4:
                customer_id = int(input("Enter Customer ID: "))
                shipping_address = input("Enter Shipping Address: ")
                repo.place_order(customer_id, shipping_address)

            elif choice == 5:
                repo.view_customers()

            elif choice == 6:
                repo.view_products()

            elif choice == 7:
                customer_id = int(input("Enter Customer ID: "))
                repo.view_cart_items(customer_id)

            elif choice == 8:
                repo.view_orders()

            elif choice == 9:
                customer_id = int(input("Enter Customer ID to Delete: "))
                repo.delete_customer(customer_id)

            elif choice == 10:
                product_id = int(input("Enter Product ID to Delete: "))
                repo.delete_product(product_id)

            elif choice == 11:
                customer_id = int(input("Enter Customer ID: "))
                product_id = int(input("Enter Product ID to Remove from Cart: "))
                repo.remove_from_cart(customer_id, product_id)

            elif choice == 12:
                customer_id = int(input("Enter Customer ID to View Orders: "))
                repo.view_orders_by_customer(customer_id)
            elif choice == 13:
                try:
                    order_id = int(input("Enter Order ID to remove: "))
                    repo.remove_order(order_id)  # Correct Call
                except Exception as e:
                    print("Error:", e)
                 

            elif choice == 14:
                print("Thank You for using E-Commerce App!")
                break

            else:
                print("Invalid choice! Enter a valid one.")

        # Exception Handling starts here
        except CustomerNotFoundException as cne:
            print("Error:", cne)

        except ProductNotFoundException as pne:
            print("Error:", pne)

        except OrderNotFoundException as one:
            print("Error:", one)

        except ValueError:
            print("Invalid input! Please enter correct values.")

        except Exception as e:
            print("Unexpected Error:", e)


if __name__ == "__main__":
    main()
