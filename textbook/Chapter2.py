# Converting Celsius temperature to Fahrenheit

def main():
    celsius = eval(input("WHat is the Celsius temperature: "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()

# Average 2 exam scores 

def main(): 
    print("This program computes the average of 2 exam scores.")

    score1, score2 = eval(input("Enter 2 scores separated by a comma: "))
    average = (score1 + score2) / 2

    print("THe average of the scores is:", average)

main()

# computing the value of an investment carried 10 years into the future 

def main(): 
    print("This program calculates the future value")
    print("of a 10 year investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range(10):
        principal = principal * (1 + apr)
    print("The value in 10 years is:", principal)

main()