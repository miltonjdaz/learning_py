""" Section 6 Rep 6 """ 

# Triangle program with functions 

import math

def totalarea(a, b, c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def main():
    print("This program calculates the are of a triangle.")
    print()

    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    
    area = totalarea(a, b, c)

    print()
    print("The area is", area, "square units.")

main()