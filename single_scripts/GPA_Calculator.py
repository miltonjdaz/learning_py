# Author: Milton D'az
# File: GPA_Calculator.py
#
# A program calculates the GPA of a student

def intro():
	print("GPA Calculator")

def calc_gpa():
	num_classes = int(input("How many classes are you taking: "))
	total_credit_hours = 0
	credit_hours = 0
	quality_points = 0
	total_quality_points = 0
	for i in range(num_classes):
		letter_grade = input("What is the letter grade: ")
		letter_int = translate(letter_grade)
		credit_hours = int(input("What are the credit hours for that class: "))
		quality_points = letter_int * credit_hours
		total_quality_points = total_quality_points + quality_points
		total_credit_hours = total_credit_hours + credit_hours
	GPA = total_quality_points / total_credit_hours
	return GPA

def translate(letter_grade):
	if letter_grade == 'A':
		return 4
	if letter_grade == 'B':
		return 3
	if letter_grade == 'C':
		return 2 
	if letter_grade == 'D':
		return 1 
	if letter_grade == 'F':
		return 0 
	return numeric_grade
	
def main():
	intro()
	GPA = calc_gpa()
	print("Your GPA is", GPA)
main()
