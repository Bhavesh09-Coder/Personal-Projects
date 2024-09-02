class Restaurant_management_system:
    def __init__(self):
        # Initialize the menu with default items and their prices
        self.menu = {
            "Paneer Tikka": 250,
            "Chicken Biryani": 350,
            "Veg Manchurian": 180,
            "Mutton Rogan Josh": 450,
            "Dal Makhani": 220,
            "Butter Naan": 40,
            "Masala Dosa": 120,
            "Chicken Tandoori": 300,
            "Palak Paneer": 240,
            "Fish Curry": 400,
            "Mushroom Soup": 150,
            "Chole Bhature": 160,
            "Pasta Alfredo": 200,
            "Caesar Salad": 180,
            "Pav Bhaji": 140,
            "Chicken Kebab": 280,
            "Paneer Butter Masala": 260,
            "Spring Rolls": 130,
            "Gulab Jamun": 100,
            "Chocolate Brownie": 150
        }
        # Initialize lists to store the items and prices of customer's order
        self.order_item = []
        self.item_price = []
        # Set the default admin password
        self.__password = '1234'
        # Start the system by asking if the user is an admin or customer
        self.admin_or_customer()

    def admin_or_customer(self):
        # Main menu for choosing between admin or customer mode
        while True:
            print("""
====> Welcome to  <=====
1.Admin
2.Customer
3.Exit
             """)
            choice = input("Enter your choice: ")

            if choice == "1":
                # If admin, prompt for password
                password = input("Enter the password: ")
                if password == self.__password:
                    print("Login successful")
                    # Grant access to manage the menu
                    self.Manage_menu()
                else:
                    print("Incorrect password")
                    self.admin_or_customer()
                
            elif choice == "2":
                # If customer, allow them to place an order and print the bill
                self.customer_order()
                self.print_bill()
            
            elif choice == "3":
                # Exit the system
                print("Thanks!!")
                break
            else:
                print("Enter a valid choice")
            
    def Manage_menu(self):
        # Menu management options for the admin
        while True:
            print("""
====> Restaurant Management System <====
1.Add Menu
2.Remove Menu
3.Update Menu
4.Display Menu
5.Exit Menu
                 """)
            choice = input("Enter your choice: ")
            
            if choice == '1':
                # Add a new item to the menu
                self.add_menu()

            elif choice == '2':
                # Remove an existing item from the menu
                self.remove_menu()

            elif choice == '3':
                # Update the price of an existing menu item
                self.update_menu()

            elif choice == '4':
                # Display the current menu
                self.display_menu()
                
            elif choice == '5':
                # Exit menu management
                print('Thank you!!')
                break    
            else:
                print("Enter valid input")

    def add_menu(self):
        # Add a new item to the menu
        item_name = input("Enter item name to menu: ").strip().title()
        price = int(input("Enter price of item: "))
        self.menu[item_name] = price
        print('The menu has been added')

    def remove_menu(self):
        # Remove an item from the menu
        print(self.menu)
        item = input("Enter the item you want to remove: ").title().strip()
        del self.menu[item]
        print("The item has been removed")

    def update_menu(self):
        # Update the price of an existing item in the menu
        print(self.menu)
        item = input("Enter the item you want to update: ").title().strip()
        price = float(input("Enter the new price: "))
        if item in self.menu:
            self.menu[item] = price
            print("The item has been updated")
        else:
            print("The item is not in the menu!!")

    def display_menu(self):
        # Display the menu with items and their prices
        for name, price in self.menu.items():
            print(f'{name} --> price: {price}$')
         
    def customer_order(self):
        # Allow customer to place an order by selecting items from the menu
        self.display_menu()
        order = input("Enter your order items (separate by commas): ").title().split(",")

        for i in order:
            item = i.strip() 
            if item in self.menu:
                # Add the selected item and its price to the order
                self.order_item.append(item)
                self.item_price.append(self.menu[item])
            else:
                print(f"Sorry, {item} is not available in the menu.")

    def print_bill(self):
        # Print the bill with the total amount
        print('===> Bill <===')
        for item, price in zip(self.order_item, self.item_price):
            print(f'{item} --- {price}$')
        total = sum(self.item_price)
        print(f"\nTotal Amount: {total}$")
  
# Instantiate the Restaurant_management_system class to start the program
r1 = Restaurant_management_system()
