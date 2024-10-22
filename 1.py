def calculate(age,Tickets):

    if age>=60:
        Ticketp = 30

    elif age<=12:
        Ticketp = 20

    else:
        Ticketp = 50

    total_cost = Ticketp * Tickets
    return total_cost

age = int(input("Enter age: "))
Tickets = int(input("no of pansenger"))

total_cost = calculate(age , Tickets)


print(f"The total cost for {Tickets} tickets is: Rs.{total_cost}")