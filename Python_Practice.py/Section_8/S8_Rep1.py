""" Section 8 Rep 1 """

# Nth fibonacci with loop 

def main():
    n = int(input("The value of n: "))
    curr, prev = 1, 1
    for i in range(n-2):
        curr, prev = curr + prev, curr

    print("The nth Fibonacci number is", curr)

if __name__ == '__main__':
    main()