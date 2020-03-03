""" Section 6 Rep 4 """ 

# Sum of n numbers using functions 

import math

def sumN(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
    return total 

def sumNCubes(n):
    total = 0
    for i in range(1,n+1):
        total = total + i**3
    return total 

def main():
    n = int(input("Please enter a value for n: "))
    print("The sum of the first %d natural numbers is %d" % (n,sumN(n)))
    print("The sum of the cubes of those numbers is %d" % (sumNCube(n)))

main()