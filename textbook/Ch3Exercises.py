# Finding the cost of an order 

def main(): 
    pounds = eval(input("How many pounds of coffee do you want: "))
    cost = (10.50 * pounds) + (.86 * pounds) + 1.50
    print("The cost of your order is:", cost)

main()

def cal():
    n = int(input("How many numbers do you want to add? "))
    sum = 0 
    for i in range(n):
        value = int(input("Enter next num: "))
        sum = sum + value
        average = round(sum/n, 2)
    print()
    print(average)

cal()