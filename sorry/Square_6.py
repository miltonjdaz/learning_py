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