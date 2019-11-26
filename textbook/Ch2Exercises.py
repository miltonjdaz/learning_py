# Average 3 exam scores 

def main(): 
    print("This program computes the average of 3 exam scores.")

    score1, score2, score3 = eval(input("Enter 3 scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3

    print("THe average of the scores is:", average)

main()

# computing the value of an investment carried a certain number of years into the future 

def main(): 
    print("This program calculates the future value")
    print("of a 10 year investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    x = eval(input("Enter the number of years of investment: "))

    for i in range(x):
        principal = principal * (1 + apr)
    print("The value in" x "years is:", principal)

main()

# kilometers to miles
def main(): 
    kilometer = eval(input("How many kilometers: "))
    miles = 1.60934 * kilometer 
    print("The amount of miles is", miles, "miles.")

main() 