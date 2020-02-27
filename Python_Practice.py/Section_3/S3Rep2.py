""" Section 3 Rep 2 """

# Program to calculate the cost per square inch of a circular pizza

import math

def main(): 
    diam = float(input("What is the diameter: "))
    price = float(input("What is the price of the pizza: "))

    Area = math.pi * (diam/2.0)**2 

    cost = price/Area
    
    print()
    print("The cost per square inch is:", cost)

main()