# Sphere
import math

def main():
    r = float(input("Enter the radius: "))
    V = 4/3 * math.pi * r ** 3
    A = 4 * math.pi * r ** 2
    print("The volume of this sphere is", V)
    print("The area of this sphere is", A) 
    
main()

def dos():
    d = float(input("What is the diameter: "))
    price = float(input("What is the price of the pizza: "))
    r = d / 2 
    A = math.pi * r ** 2 
    cost_per = price / A 
    print("The cost per square inch is:", cost_per)

dos()