# Simple string processing program to generate usernames. 

def main(): 
    print("This program generates computer usernames.\n")

    # get user's first and last names 
    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")

    # concatenate first initial with 7 chars of the last name. 
    uname = first[0] + last[:7]

    # output the username 
    print("Your username is:", uname)

main() 

# A program to print the abbreviation of a month, given its number 

def main2():
    # months is used as a lookup table 
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = int(input("Enter a month number (1-12): "))

    # compute starting position of month n in months 
    pos = (n-1) * 3 

    # grab the appropriate slice from months 
    monthAbbrev = months[pos:pos+3]

    # print the result 
    print("The month abbreviation is", monthAbbrev + ".")

main2()

# A program to print the month abbreviation, given its number 

def main3(): 
    # months is a list used as a lookup table 
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    n = int(input("Enter a month number (1-12): "))

    print("The month abbreviation is", months[n-1] + ".")

main3() 
