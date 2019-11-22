# Modified chaos function 

def main(): 
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x* (1-x) 
        print(x)
main()

# Output must be 20 

def main(): 
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 3.9 * x* (1-x) 
        print(x)
main()

# Number of values printed is determined by user 

def main(): 
    print("This program illustrates a chaotic function")
    n = eval(input("How many numbers should I print: "))
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(n):
        x = 3.9 * x* (1-x) 
        print(x)
main()

