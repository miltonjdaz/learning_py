# Author: Milton D'az
# File: Car_Driver.py
#
# A program tells you the make, model, year, and odometer of a car 
class Car: 
	"""This class returns all the values needed to produce the correct output"""
	def __init__(self, make, model, year, odometerReading):
		self.make = make
		self.model = model
		self.year = year
		self.odometerReading = odometerReading
		
	def getMake():
		return self.make
	def getModel():
		return self.model
	def getYear():
		return self.year
	def getOdometerReading():
		return self.odometerReading
	def __str__(self):
		return str(self.year) + " " + self.make + " " + self.model + " with " + str(self.odometerReading) + " miles"
def main():
	"""This method asks for input for the values required"""
	make = str(input("What's your car's make?"))
	model = str(input("What's your car's model?"))
	year = int(input("What's your car's year?"))
	while True:
		mileage = float(input("What is the mileage?"))
		if mileage > 100000:
			print("Time for a new car")
			break
	mycar = Car(make, model, year, mileage)
	print(mycar)
main()