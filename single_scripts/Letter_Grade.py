# Author: Milton D'az
# File: Letter_Grade.py
#
# A program that converts an exam score to a letter grade

def numeric_input():
	score = float(input("What is your exam score: "))
	return score

def processing(score):
	if score >= 90 and score <= 100:
		return("Your grade is: A")
	elif score >= 80 and score < 90:
		return("Your grade is: B")
	elif score >= 70 and score < 80:
		return("Your grade is: C")
	elif score >= 60 and score < 70:
		return("Your grade is: D")
	else:
		return("Your grade is: F")

def output(grade):
	print(grade)

def main():
	try:
		numeric_grade = numeric_input()
		letter_grade = processing(numeric_grade)
		output(letter_grade)
	except:
		print("You must enter a number.")
main()