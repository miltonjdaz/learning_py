""" Section 7 Rep 1 """

# Program figuring out pay

def main(): 
    hours = float(input("How many hours did you work: "))
    rate = float(input("How much do you get paid an hour: "))

    if hours <= 40:
        pay = hours * wage
    else: 
        pay = 40 * wage + (hours - 40) * 1.5 * wage 

    print("Your week's pay is ${0:0.2f}".format(pay))

if __name__ == '__main__':
    main()