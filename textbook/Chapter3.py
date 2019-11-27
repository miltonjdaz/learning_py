# to calculate the value of some change 

def main(): 
    print("CHange COunter")
    print()
    print("Please enter the count of each coin type.")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01 
    print()
    print("The total value of your change is", total)

main() 

# Python built in numeric operations 
# operator  operation
#    +      addition
#    -      subtraction
#    *      multiplication 
#    /      float division 
#    **     exponentiation
#    abs()  absolute value
#    //     integer division 
#    %      remainder 

# Using int instead of eval in the input statements ensures that the user will only enter whole numbers 

# Computing the real roots of a quadratic equation 
# You will be using the math library 

import math 

def main(): 
    print("This program finds the real solution to a quadratic")
    print()

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discRoot = math.sqrt(b * b -4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print("The solutions are:", root1, root2 )

main() 

# The following is to compute the factorial of a number 

def main(): 
    n = int(input("Please enter a whole number: "))
    fact = 1 
    for factor in range(n,1,-1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)

main() 