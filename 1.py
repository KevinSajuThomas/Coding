def calculate(age, tickets):
    if age >= 60:
        ticket_price = 30
    elif age <= 12:
        ticket_price = 20
    else:
        ticket_price = 50
    total_cost = ticket_price * tickets
    return total_cost

age = int(input("Enter age: "))
tickets = int(input("Number of passengers: "))

total_cost = calculate(age, tickets)
print(f"The total cost for {tickets} tickets is: Rs.{total_cost}")
