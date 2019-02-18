# Author: Milton D'az
# File: CampusGPA.py
#
# A program that finds the average of students GPA.

def main():
	total = 0.0
	count = 0 
	while True: 
		number = float(input("Enter a positive number (-1 to quit): "))
		if (number < 0):
			break
		total = total + number
		count = count + 1
	print("The average GPA is:", (round((total/count), 2)))
	print("Number of students:", count)
main()