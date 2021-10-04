def main():
    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3.0 

    print(average)

main()

def dos():
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature: "))
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print()

dos()

def tres():
    for celsius in [10,20,30,40,50,60,70,80,90]:
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print(celsius, "        ", fahrenheit)
    print("100         212.0")

tres()

def four():
    principal = eval(input("Enter the principal: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The amount in", years, "years is:", principal)

four()

def five():
    payment = eval(input("Enter amount to invest each year: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: "))

    principal = 0.0
    for i in range(years):
        principal = (principal + payment) * (1 + apr)

    print("The amount in", years, "years is:", principal)

five()

def six():
    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the interest rate: "))
    periods = eval(input("Enter the number of compounding periods per year: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years * periods):
        principal = principal * (1 + rate/periods)

    print("The amount in", years, "years is:", principal)

six()