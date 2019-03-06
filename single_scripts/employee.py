# Author: Milton D'az
# File: employee.py
#
# A program that determines people's pay at a company

class Employee:
	"""This class determines the regular pay of an employee"""
	def __init__(self, id, name, rate):
		self.id = id 
		self.name = name
		self.rate = rate
		
	def getID(self):
		return self.id 
	
	def getName(self):
		return self.name
		
	def getRate(self):
		return self.rate
	
	def pay(self):
		return self.rate * 40
	
	def __str__(self):
		return str(self.id) + " " + self.name 
		
class SalariedEmployee(Employee):
	"""This super class determines the salaried pay of an employee"""
	def __init__(self, id, name, salary):
		Employee.__init__(self, id, name, 0)
		self.salary = salary
	# getter and setter for salary 
	def setSalary(self, newSalary):
		self.salary = newSalary
		
	def getSalary(self):
		return self.salary 
	
	def pay(self):
		return self.salary / 12.0
		
def main():
	e123 = Employee(123, "Joe", 14)
	e987 = Employee(987, "Jon", 17)
	e234 = SalariedEmployee(234, "Sally", 240000)
	e567 = SalariedEmployee(567, "Wally", 480000)
	
	print("==========================================")
	print("The following are the highest and lowest pay:")
	
	elist = [e123, e987, e234, e567]
	high = elist[0].pay()
	for e in elist:
		if e.pay() > high:
			high = e.pay()
	print(high)
	
	low = elist[0].pay()
	for e in elist:
		if e.pay() < low:
			low = e.pay()
	print(low)
	
	print("==========================================")
	print("The following are the names & id of the employees:")
	
	elist.sort(key=Employee.getName)
	for i in elist:
		print(i)
	
	print("==========================================")
	print("The following are the different pay for each employee:")
	
	lookup = {123: e123, 987: e987, 234: e234, 567: e567}
	for x in lookup:
		print(lookup.get(x).pay())
	print("==========================================")
main()