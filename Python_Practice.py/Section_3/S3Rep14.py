""" Section 3 Rep 14 """ 

# Program that finds the average of numbers entered by user

def main(): 
    numbers = int(input("How many numbers do you want to add: "))
    total = 0.0
    for i in range(numbers): 
        num = float(input("What is the next number: "))
        total = total + num

    final = total / numbers 
    print("The average of the numbers is:", final)

main()