# This program finds the average of numbers put in by the user

def main():
    n = int(input("How many numbers do you have? "))
    total = 0.0 
    for i in range(n): 
        x = float(input("Enter a number >> "))
        total = total + x 
    print("\nThe average of the numbers is", total / n)

main()

def more():
    total = 0.0
    count = 0 
    moredata = "yes"

    while moredata[0] == "y": 
        x = float(input("Enter a number >>"))
        total = total + x 
        count = count + 1 
        moredata = input("Do you have more numbers (yes or no)? ")
    print("\nThe average of the bumbers is", total / count)

more()

def neg(): 
    total = 0.0
    count = 0 
    x = float(input("Enter a number (negative to quit) >> "))
    while x >= 0: 
        total = total + x 
        count = count + 1 
        x = float(input("Enter a number (negative to quit) >> "))
    print("\nThe average of the bumbers is", total / count)

main() 