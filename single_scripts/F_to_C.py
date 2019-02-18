# Author: Milton D'az
# File: F_to_C.py
#
# A program calculating Celsius from Fahrenheit

def main():
	Fahrenheit = eval(input("Enter the temperature in degrees F: "))
	Celsius = round (((Fahrenheit - 32) * (5/9)), 2)
	print ("The temperature is", Celsius, "degrees C")
main() 