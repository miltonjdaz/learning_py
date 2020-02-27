""" Section 3 Rep 7 """

# Program to find the distance between 2 points 

import math

def main(): 
    x1 = float(input("What is the point for x1: "))
    x2 = float(input("What is the point for x2: "))
    print()
    y1 = float(input("What is the point for y1: "))
    y2 = float(input("What is the point for y2: "))

    distance = math.sqrt((x2 - x1)**2 +(y2 - y1)**2)

    print("The distance between 2 points is:", distance)

main()