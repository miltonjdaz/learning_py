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

# A program to convert a text message into a sequence of numbers using Unicode

def main4(): 
    # get the message to encode 
    message = input("Please enter the message to encode: ")

    print("\nHere are the Unicode codes:")

    # loop through the message and print out the Unicode values 
    for ch in message: 
        print(ord(ch), end=" ")

    print() # blank line before prompt 

main4() 

# A program to convert a sequence of Unicode numbers into a string of text. 

def main5(): 
    # get the message to encode 
    inString = input("Please enter the Unicode-encoded message: ")

    # loop through each substring and build Unicode message 
    message = ""
    for numStr in inString.split():
        codeNum = int(numStr)               # convert digits to a number
        message = message + chr(codeNum)    # concatentate character to message 
    print("\nThe decoded message is:", message)

main5()

# Unicode numbers into a string of text using efficient version using a list accumulator. 

def main6():
    # get message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    # loop through each substring and build Unicode message 
    chars = [] 
    for numStr in inString.split():
        codeNum = int(numStr)           # convert digits to a number 
        chars.append(chr(codeNum))      # accumulate new character

    message = "".join(chars)
    print("\nThe decoded message is:", message)

main6() 

# Converts a date in form "mm/dd/yyyy" to "month day, year"

def main7(): 
    # get the date
    dateStr = input("Enter a date (mm/dd/yyyy): ")

    # split into components 
    monthStr, dayStr, yearStr = dateStr.split("/")

    # convert monthStr to the month name 
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August", 
              "September", "October", "November", "December"]
    monthStr = months[int(monthStr)-1]

    # output result in month day, year format 
    print("The converted date is:", monthStr, dayStr+",", yearStr)

main7()

# A program to calculate the value of some change in dollars, this version represents the total cash in cents. 

def change2(): 
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))

    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies

    print("The total value of your change is ${0}.{1:0>2}"
          .format(total//100, total%100))

change2()

# Prints a file to the screen

def main8():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)

main8()

# Program to create a file of usernames in batch mode 

def main9(): 
    # get the file names 
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")

    # open the files 
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file 
    for line in infile: 
        # get the first and last names from line 
        first, last = line.split()

        # create the username
        uname = (first[0]+last[:7]).lower()

        # write it to the output fle 
        print(uname, file=outfile)
    
    # close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)

main9()