""" Section 3 Rep 13 """ 

# Program to find total of numbers entered by user 

def main(): 
    numbers = int(input("How many numbers do you want to add: "))
    total = 0.0
    for i in range(numbers): 
        num = float(input("What is the next number: "))
        total = total + num 
    print("The sum of the numbers is:", total)

main()