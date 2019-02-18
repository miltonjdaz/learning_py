# Author: Milton D'az
# File: colorcar.py
#
# A program about multiple cars and their tires & colors

class car:
	"""This class returns all the values needed to produce the correct output"""
	def __init__(self, color):
		self.color = color 
		self.tires = 4

	def getNumTires(self):
		return self.tires
	
	def getColor(self):
		return self.color

	def drive(self):
		if self.tires == 4:
			print(self.color + " " + "car goes vroom!") 
		else:
			print(self.color + " " + "car cannot drive!")
			
	def flat(self):
		if self.tires > 0:
			self.tires = self.tires - 1 
			
	def __str__(self):
		return ("A " + self.color + " car with " + str(self.tires) + " " + "tires.")
		
def main():
	cars = []
	c1 = car("red")
	c1.drive()
	cars.append(c1)

	c2 = car("beige")
	c2.flat()
	c2.flat()
	c2.drive()
	cars.append(c2)

	c3 = car("gray")
	c3.flat()
	c3.flat()
	c3.flat()
	c3.drive()
	cars.append(c3)

	print("==========================================")
	
	cars.sort(key = car.getColor)
	for c in cars:
		print(c)
		
	print("==========================================")
	
	cars.sort(key = car.getNumTires)
	for c in cars:
		print(c)

	print("==========================================")

	c4 = car("neon")
	c5 = car("yellow")
	c6 = car("purple")
	c7 = car("crimson")
	
	lookup = {"Fran": c4, "Alice": c5, "Bob": c6, "Ted": c7}
	print(lookup.get("Bob"))
	
main()