# Author: Milton D'az
# Date: 2/13/2019
# File: average.py
#
# A program asking someone how many numbers they want to average.
 
def main():
	n = int(input("How many numbers do you want to add? "))
	sum = 0 
	for n in range(n):
		value = int(input("Enter next num: "))
		sum = sum + value
		average = round(sum/n, 2)
	print()
	print(average)

main()
input("Press the <Enter> key to quit.") 