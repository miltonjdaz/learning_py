""" Section 3 Rep 8 """

# Program that outputs the value of the epact 

def main(): 
    year = int(input("What is the year (e.g. 2000): "))

    C = year//100
    epact = (8 + (C//4) - C + ((8C + 13)//25) + 11*(year%19))%30

    print("The epact is:", epact)

main()