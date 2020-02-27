""" Section 3 Rep 6 """

# Program to find the slope of 4 points 

def main(): 
    x1 = float(input("What is the point for x1: "))
    x2 = float(input("What is the point for x2: "))
    print()
    y1 = float(input("What is the point for y1: "))
    y2 = float(input("What is the point for y2: "))

    slope = (y2 - y1) / (x2 - x1)

    print("The slope is:", slope)

main()