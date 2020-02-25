""" Section 2 Rep 4 """

# 

def main():
    print("This program calculates the future value")
    print("of a specific amount of years investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the amount of years invested: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in", years, " years is:", principal)

main()