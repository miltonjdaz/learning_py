# Author: Milton D'az
# File: mileage.py
#
# A program calculates the miles per gallon

def get_data():
	start = float(input("Enter the starting odometer: "))
	end = float(input("Enter the ending odometer: "))
	gas = float(input("Enter the amount of gallons used: "))
	return (start, end, gas)
	
def calculate_mpg(start, end, gas):
	try:
		mpg = (end - start) / gas
		return mpg
	except:
		return 0

def main():
	try:
		start, end, gas = get_data()
		mpg = calculate_mpg(start, end, gas) 
		if mpg > 0:
			print(mpg)
		else:
			print("Error: You cannot divide by 0")
	except:
		print("Error: You must enter a number.")
main()