# cafe.py
# Name: Nayeon Kim
# Student ID: u3309753
# Date: 17-09-2025

def show_menu(menu):
    # Print all items, prices, and categories
    pass

def add_item(cart, menu):
    # Ask for item name
    # If item in menu:
    #   Ask for quantity
    #   Add (item, quantity, price) to cart
    # Else:
    #   Print "Item not found"
    pass

def view_cart(cart):
    # Display contents of the cart
    pass

def checkout(cart):
    # Calculate subtotal
    # Calculate tax (10%)
    # Ask if student → apply discount (5%) if yes
    # If both food and drink in cart → apply meal deal (optional)
    # Print receipt (items, quantities, prices, totals)
    pass

def main():
    menu = {
        "Coffee": {"price": 3.5, "category": "Drink"},
        "Tea": {"price": 3.0, "category": "Drink"},
        "Sandwich": {"price": 6.0, "category": "Food"},
        "Muffin": {"price": 4.0, "category": "Food"},
        "Juice": {"price": 3.8, "category": "Drink"},
        "Salad": {"price": 5.5, "category": "Food"},
    }
    cart = []
    
    while True:
        print("\n1. Show Menu\n2. Add Item\n3. View Cart\n4. Checkout\n5. Exit")
        choice = input("Select option (1–5): ").strip()

        if choice == "1":
            show_menu(menu)

        elif choice == "2":
            add_item(cart, menu)

        elif choice == "3":
            view_cart(cart)

        elif choice == "4":
            checkout(cart)
            break  # End the loop after checkout

        elif choice == "5":
            break  # Exit the program

        else:
            print("Invalid selection. Please choose 1–5.")

if __name__ == "__main__":
    main()

