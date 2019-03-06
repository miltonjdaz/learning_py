# Author: Milton D'az
# File: liters_to_gallons.py
#
# This program converts liters to gallons 

print("The following is a converter of liters to gallons from 1 - 10") 

def main():
	for i in range(10): 
		liters = i + 1
		gallons = liters * 0.264172
		print(liters,"\t",gallons)
	input("Press the <Enter> key to quit.")
main()
