# Average 

def main():
    n = int(input("How many numbers do you have? "))
    total = 0.0
    for i in range(n):
        x = float(input("Enter a number: "))
        total = total + x
    print("\nThe average of the numbers is", total / n)
    
main()

# Nth fibonacci with loop 

def dos():
    n = int(input("The value of n: "))
    curr, prev = 1, 1
    for i in range(n-2):
        curr, prev = curr + prev, curr

    print("The nth Fibonacci number is", curr)

dos()