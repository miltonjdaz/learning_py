""" Section 3 Rep 12 """

# Program to find the sum of the cubes of the first n natural numbers 

def main(): 
    n = int(input("Please enter a value for n: "))
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**3

    print()
    print("The sum from 1 to", n, "is:", sum)

main()