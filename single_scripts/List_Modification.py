# Author: Milton D'az
# File: List_Modification.py
#
# A program changing str to int

def toNumbers(strList):
	print("List after call:", [24,45])
	for i in strList:
		var = int(i)
		print(var, "is a", type(var))
	return var


def main():
	numbers = '24', '45'
	print("List before call:", list(numbers))
	print("24 is a", type ('24'))
	print("45 is a", type ('45'))
	toNumbers(numbers)
main()
