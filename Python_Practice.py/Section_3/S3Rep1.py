""" Section 3 Rep 1 """

# Program to calculate the volume & surface area of a sphere 

import math 

def main(): 
    r = float(input("What is the radius: "))

    v = (4.0/3.0) * math.pi * r**3
    a = 4 * math.pi * r**2 

    print("The volume is: ", v)
    print()
    print("The area is: ", a)

main()