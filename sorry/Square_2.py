# Converts Celsius temps to Fahrenheit 

def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    
main()

def dos():
    print("This program calculates the future value of an investment.")
    print()
    
    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the interest rate: "))
    periods = eval(input("Enter the number of compounding periods per year: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years * periods):
        principal = principal * (1 + rate/periods)

    print("The amount in", years, "years is:", principal)

dos()

def three():
    kilometers = eval(input("How many kilometers? "))
    miles = 0.62 * kilometers
    print("This is the distance in miles:", miles) 

three()

def quad():
    print("This program computes the average of 3 scores.")

    score1, score2, score3 = eval(input("Enter 3 scores separated by a comma: "))
    average = (score1 + score2 + score3)/ 3.0

    print("The average of the scores is:", average)

quad()