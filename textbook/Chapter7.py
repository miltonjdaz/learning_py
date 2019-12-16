# A program to convert Celsius temperature to Fahrenheit & it has warning messages

def main():
    celsius = float(input("What is the Celsius temperature: "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    # print warnings for dangerous temperatures
    if fahrenheit > 90:
        print("It's super hot out there. Be careful!")
    if fahrenheit < 30: 
        print("Put on your winter coat!")

main() 

import math

def quad():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("\nThe equation has no real roots!")
    elif discrim == 0:
        root = -b / (2 * a)
        print("\nThere is a double root at", root)
    else: 
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2 )

quad() 

# Using the try 

import math 

def quad2():
    try: 
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2 )
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No real roots")
        else:
            print("Invalid coefficient given")
    except:
        print("\nSomething went wrong, sorry")

quad2() 

# Finds the maximum of a series of numbers 

def mainmax(): 
    n = int(input("How many numbers are there: "))

    # set max to be the first value 
    maxval = float(input("Enter a number >> "))

    # compare the n-1 successive values 
    for i in range(n-1):
        x = float(input("Enter a number >> "))
        if x > maxval: 
            maxval = x 
    print("The largest value is", maxval)

mainmax() 