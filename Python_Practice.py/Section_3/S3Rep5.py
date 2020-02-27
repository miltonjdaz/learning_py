""" Section 3 Rep 5 """

# Program to calculate the cost of an order of coffee 

def main():
    pounds = float(input("How many pounds of coffee: "))
    
    coffee_cost = pounds * 10.50
    ship_cost = (pounds * 8.6) + 1.50 
    total_cost = ship_cost + coffee_cost

    print("The cost of coffee is:", coffee_cost)
    print("The cost of shipping is:", ship_cost)
    print("The total cost is:", total_cost)

main()
