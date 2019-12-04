# Finding the cost of an order 

def main(): 
    pounds = eval(input("How many pounds of coffee do you want: "))
    cost = (10.50 * pounds) + (.86 * pounds) + 1.50
    print("The cost of your order is:", cost)

main()

def cal():
    n = int(input("How many numbers do you want to add? "))
    sum = 0 
    for i in range(n):
        value = int(input("Enter next num: "))
        sum = sum + value
        average = round(sum/n, 2)
    print()
    print(average)

cal()

import math 

def vanda(): 
    r = int(input("What is the length of the radius: "))
    V = (4/3)*(math.pi)*(r^3)
    A =  (4)*(math.pi)*(r^2)
    print("The volume of the sphere is:", V)
    print("The surface area of the sphere is:", A)

vanda() 

def light(): 
    sec = int(input("How many have seconds passed: "))
    sos = 1100 * sec
    miles = float(sos / 5280)
    print("The amount of miles from the lightning strike is:", miles, "miles")

light()


def tri(): 
    a = int(input("The length of side a: "))
    b = int(input("The length of side b: "))
    c = int(input("The length of side c: "))
    s = (a + b + c) / 2 
    A = float(math.sqrt(s*(s-a)*(s-b)*(s-c)))
    print("The area of a triable is:", A)

tri()