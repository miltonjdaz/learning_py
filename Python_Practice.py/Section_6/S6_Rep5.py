""" Section 6 Rep 5 """

# Pizza with functions 

import math

def piesize(d):
    return math.pi * (0.5*d)**2

def dollar(d, price):
    return float(price) / piesize(d)

def main():
    diam = float(input("Enter the diameter of the pizza (in inches): "))
    price = float(input("Enter the price of the pizza (in cents): "))
    
    print("\nThe pizza costs %0.4f per square unit." % (dollar(diam,cost)))

main()