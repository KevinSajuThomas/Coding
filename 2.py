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

    if total_cost >= 500:
        total_cost *= 0.90

    print(f"You ordered {enter_quantity} {food_item} for a total cost of Rs {total_cost}")
else:
    print("Invalid choice. Please select a number between 1 and 5")


"""
prolem 2:

Anil is ordering some food from a menu. In the menu cart it is displaying all the food items with their prices.

Food items :
1.Pizza - Rs.200
2.Burger - Rs.100
3.Dosa - Rs.150
4.Briyani - Rs.250 
5.Chicken rice - Rs.200

if the order total exceeds Rs.500, apply for 10% discount.Find out the total cost of the order , including
any applicable discounts.
"""
