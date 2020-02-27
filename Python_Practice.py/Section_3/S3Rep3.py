""" Section 3 Rep 3 """

# Program to calculate the molecular weight 

def main():
    hydrogen = int(input("Enter the number of hydrogen atoms: "))
    carbon = int(input("Enter the number of carbon atoms: "))
    oxygen = int(input("Enter the number of oxygen atoms: "))

    total_weight = (hydrogen*1.00794) + (carbon*12.0107) + (oxygen*15.9994)

    print("The total weight is:", total_weight)

main()