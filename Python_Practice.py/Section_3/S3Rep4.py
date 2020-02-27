""" Section 3 Rep 4 """

# Program to determine the distance to a lightning strike 

def main():
    seconds = int(input("How many seconds went by: "))

    one_mile = 5280.0

    distance = seconds * 1100

    total_miles = distance / one_mile 

    print("The number of miles between strike and you is:", round(total_miles, 1)

main()