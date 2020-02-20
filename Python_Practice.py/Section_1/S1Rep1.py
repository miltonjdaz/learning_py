""" Section 1 Rep 1"""

# Program with a chaotic function

def main(): 
    print("This program illustrates a chaotic funciton")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers do you want? "))
    for i in range(n):
        x = 3.9 * x * (1-x)
        print(x)

main()