# If

def main():
    celsius = float(input("What is the Celsisu temperature? "))
    fahrenheit = 9/5 * celsius + 32 
    print("The temperature is", fahrenheit, "degrees Fahrenheit")

    # Warnings for extreme temperatures 
    if fahrenheit > 90:
        print("Drink more water, it is hot today")
    if fahrenheit < 30:
        print("Bundle up, it is cold today")

main()

def dos():
        hours = float(input("How many hours did you work: "))
    wage = float(input("How much do you get paid an hour: "))

    if hours <= 40:
        pay = hours * wage
    else: 
        pay = 40 * wage + (hours - 40) * 1.5 * wage 

    print("Your week's pay is ${0:0.2f}".format(pay))

dos()