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

"""
problem 1:

The person is booking the railway ticket based on their age and the number of tickets they want to purchase.The 
prices are regular price : rs.50, senior citizen (Age 60 and above) price : rs.30 and for the children 
age 12 and below price is :rs.20.Find out total cost based on the their age and the number of tickets and display it.

"""
