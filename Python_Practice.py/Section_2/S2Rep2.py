""" Section 2 Rep 2 """

# Simple program to find the average of 3 scores

def main():
    print("This program computes the average of 3 scores.")

    score1, score2, score3 = eval(input("Enter 3 scores separated by a comma: "))
    average = (score1 + score2 + score3)/ 3.0

    print("The average of the scores is:", average)

main() 