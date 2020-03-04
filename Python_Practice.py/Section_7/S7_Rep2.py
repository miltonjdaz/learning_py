""" Section 7 Rep 2 """

# Program using if for a quiz

def main():
    score = float(input("What did you get in the quiz: "))
    if score < 2:
        grade = "F"
    elif score < 3:
        grade = "D"
    elif score < 4:
        grade = "C"
    elif score < 5:
        grade = "B"
    else:
        grade = "A"
    print("Grade is", grade)

if __name__ == '__main__':
    main()
