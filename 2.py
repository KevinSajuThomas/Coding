menu = {
    1: ("Pizza", 200),
    2: ("Burger", 100),
    3: ("Dosa", 150),
    4: ("Biryani", 250),
    5: ("Chicken Rice", 200)
}

enter_choice = int(input("Enter your choice (1-5): ")) 
enter_quantity = int(input("Enter quantity: "))

if enter_choice in menu:
    food_item, price = menu[enter_choice]
    total_cost = price * enter_quantity
    print(f"You ordered {enter_quantity} {food_item} for a total cost of Rs {total_cost}")
else:
    print("Invalid choice. Please select a number between 1 and 5")