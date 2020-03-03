""" Section 5 Rep 5 """

# Program that determines a value from a name 

def main(): 
    name = input("What is your name? ")

    total = 0 
    for letter in name:
        total = total + ord(letter.lower()) - ord('a') + 1 

    print("The value is:", total)

main()