""" Section 3 Rep 9 """

# Program to calculate the area of a triangle 

import math 

def main(): 
    a = float(input("Enter the side of a: "))
    b = float(input("Enter the side of b: "))
    c = float(input("Enter the side of c: "))

    s = (a + b + c) / 2 

    Area = math.sqrt(s*(s - a)*(s - b)*(s - c))

    print("The area of a triangle is:", Area)

main()