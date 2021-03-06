# A program asking someone how many numbers they want to average.
 
def main():
	n = int(input("How many numbers do you want to add? "))
	sum = 0 
	for i in range(n):
		value = int(input("Enter next num: "))
		sum = sum + value
		average = round(sum/n, 2)
	print()
	print(average)

main()

# A program that de-codes a message.

def main():
    encodemsg = input("Enter the message to decrypt: ")
    shift = int(input("Enter the amount of the shift: "))

    encodemsg = encodemsg.split()
    sentence = []

    for word in encodemsg:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o - shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        sentence.append(plaintext)
    sentence = ' '.join(sentence)
    print (sentence)
main()

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
	e123 = Employee(123, "Milton", 14)
	e987 = Employee(987, "Claire", 17)
	e234 = SalariedEmployee(234, "Mo", 240000)
	e567 = SalariedEmployee(567, "Jo", 480000)
	
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

# A program that is a guessing game.

import random

def generate_number():
	n = random.randint (1,100)
	return n

def main():
	# input
	try:
		num_to_guess = generate_number()
	#input from end-user 
		guess = int(input("Enter a guess: "))
		while guess != num_to_guess:
			if guess < num_to_guess:
				print("Your guess is too low")
				guess = int(input("Enter a guess: "))
			elif guess > num_to_guess:
				print("Your guess is too high")
				guess = int(input("Enter a guess: "))
			else:
				guess = get_guess() 
		print("Winner chicken dinner!") 
	except ValueError:
		print("Please enter a number")
main()

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

# models 

from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'exec(%matplotlib inline)'

url = 'http://people.terry.uga.edu/rwatson/data/manheim.txt'
data = pd.read_csv(url)

# y values - numbers
xmean = data.loc[data['model']=='X', 'price'].mean()
ymean = data.loc[data['model']=='Y', 'price'].mean()
zmean = data.loc[data['model']=='Z', 'price'].mean()
yvals = [xmean, ymean, zmean]


# x values - model names
model_list = data.model.unique()
model_list.sort()

# add it all on to the blank canvas to plot
plt.bar(model_list, yvals, align='center', alpha=0.5)
plt.xlabel("model")
plt.ylabel("price")
plt.title("Average Prices for Each Model")
plt.show()

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

# A program calculating the ERA 

def calculate_era(runs, innings):
	era = (runs * 9)/innings
	return era 
def main():
	n = int(input("How many pitchers: "))
	for pitcher in range(n):
		innings = int(input("How many innings: "))
		runs = int(input("How many runs: "))
		print (round(calculate_era(runs, innings), 2))
main()

# A program that converts kilometers to miles

def main ():
	kilometers = eval(input("How many kilometers? ")) 
	miles = kilometers * 0.62137  
	print ("The kilometers converted to miles is", miles , "miles.")
main()

# A program to find specific movies in a txt

class Movie():
	def __init__(self, title, year):
		self.title = title
		self.year = year
	def getTitle(self):
		return self.title
	def getYear(self):
		return self.year
	def __str__(self):
		return str(self.year) + "\t" + self.title
def main():
	movies = []
	titles = []
	years = []
	ifs = open("movies.txt")
	line = ifs.readline()
	while line:
		data = line.split(',')
		title = data[0]
		year = int(data[1])
		m = Movie(title, year)
		movies.append(m)
		titles.append(title)
		years.append(year)
		line = ifs.readline()
	for movie in movies:
		print(movie)
	# 1.
	print(len(movies))
	print(len(years))
	print(len(movies))
	# 2.
	for movie in movies:
		if movie.getYear() == 1984:
			print(movie.getTitle())
	# 3.
	for movie in movies:
		if movie.getTitle() == "Jaws":
			print(movie.getYear())
	# 4.
	for movie in movies:
		if movie.getTitle() == "Casablanca":
			print(movie.getYear())
	# 5.
	counter = 0
	for movie in movies:
		if movie.getYear() >= 2000:
			#counter += 1
			counter = counter + 1
	print(counter)avg = (counter / len(movies)) * 100
	print("Movies since 1999 {0:.1f}%".format(avg))
	# 6.
	for movie in movies:
		#if movie.getTitle().find('Little') > -1:
		if 'Little' in movie.getTitle():
			print(movie.getTitle())
main()

from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'exec(%matplotlib inline)'

url = 'http://people.terry.uga.edu/rwatson/data/manheim.txt'
data = pd.read_csv(url)

# y values - numbers
xsum = data.loc[data['model']=='X', 'price'].sum()
ysum = data.loc[data['model']=='Y', 'price'].sum()
zsum = data.loc[data['model']=='Z', 'price'].sum()
yvals = [xsum, ysum, zsum]

# x values - model names
model_list = data.model.unique()
model_list.sort()

# add it all on to the blank canvas to plot
plt.bar(model_list, yvals, align='center', alpha=0.5, color = 'red')
plt.xlabel("model")
plt.ylabel("price")
plt.title("Sum Prices for Each Model")
plt.show()

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

# This program finds the factorial

from graphics import *

def main():
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    
    # Draw the interface
    Text(Point(1,3), "   Input n:").draw(win)
    Text(Point(1,1), "   n! is:").draw(win)
    inputText = Entry(Point(2.25,3), 5)
    inputText.setText("0")
    inputText.draw(win)
    outputText = Text(Point(2.25,1),"")
    outputText.draw(win)
    button = Text(Point(1.5,2.0),"Convert It")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)

    # wait for a mouse click
    win.getMouse()

    # convert input
    n = int(inputText.getText())
    product = 1
    for i in (range(n,0,-1)):
        product = product * i 
        print(i)

	# display output and change button
    outputText.setText(product)
    button.setText("Quit")

    # wait for click and then quit
    win.getMouse()
    win.close()
    
main()

# A program that converts an exam score to a letter grade

def numeric_input():
	score = float(input("What is your exam score: "))
	return score

def processing(score):
	if score >= 90 and score <= 100:
		return("Your grade is: A")
	elif score >= 80 and score < 90:
		return("Your grade is: B")
	elif score >= 70 and score < 80:
		return("Your grade is: C")
	elif score >= 60 and score < 70:
		return("Your grade is: D")
	else:
		return("Your grade is: F")

def output(grade):
	print(grade)

def main():
	try:
		numeric_grade = numeric_input()
		letter_grade = processing(numeric_grade)
		output(letter_grade)
	except:
		print("You must enter a number.")
main()

# A program reversing the contents of a file.

def main():
	filename = input("Enter the filename: ")
	infile = open (filename, "r")
	data = infile.read()
	print(data)
	fn_rev = filename.split(".")
	new_file = (fn_rev[0]+"_reverse."+fn_rev[1])
	print(new_file)
	opfile = open(new_file, "w")
	data[::-1]
	print(data[::-1], file=opfile)
	opfile.close()
	infile.close()
main()

# A program reads a file that stores the locations of basketball games

class Game:
	"""This lists the locations of basketball games"""
	def __init__(self, school, city, state):
		self.school = school 
		self.city = city
		self.state = state
		
	def getSchool(self):
		return self.school
		
	def getCity(self):
		return self.city
		
	def getState(self):
		return self.state
		
	def __str__(self):
		return self.school + " " + self.city + ", " + self.state
		
def main():
	games =[]
	
	input_stream = open('basketball.txt' , 'r')
	
	line = input_stream.readline()
	
	while line:
		columns = line.split(',')
		
		school = columns[0]
		city = columns[1]
		state = columns[2]
		
		b1 = Game(school, city, state)
		
		games.append(b1)
		line = input_stream.readline()
		
	
	input_stream.close()
	
	for game in games:
		print(game)

main()

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
	
	lookup = {"Milton": c4, "Claire": c5, "Roz": c6, "Jason": c7}
	print(lookup.get("Bob"))
	
main()

# A program calculating Celsius from Fahrenheit

def main():
	Fahrenheit = eval(input("Enter the temperature in degrees F: "))
	Celsius = round (((Fahrenheit - 32) * (5/9)), 2)
	print ("The temperature is", Celsius, "degrees C")
main() 

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

# This program spells out UNA Lions with dots

from graphics import *
def main ():
	win = GraphWin('UNA Lions')
	circ = Circle(Point(5, 15), 5)
	circ.setFill('yellow')
	circ.draw (win)
	circ = Circle(Point(5, 25), 5)
	circ.setFill('yellow')
	circ.draw (win)
	circ = Circle(Point(10, 35), 5)
	circ.setFill('yellow')
	circ.draw (win)
	circ = Circle(Point(20, 35), 5)
	circ.setFill('yellow')
	circ.draw (win)
	circ = Circle(Point(25, 25), 5)
	circ.setFill('yellow')
	circ.draw (win)
	circ = Circle(Point(25, 15), 5)
	circ.setFill('yellow')
	circ.draw (win)
	circ = Circle(Point(40, 15), 5)
	circ.setFill('purple')
	circ.draw (win)
	circ = Circle(Point(40, 25), 5)
	circ.setFill('purple')
	circ.draw (win)
	circ = Circle(Point(40, 35), 5)
	circ.setFill('purple')
	circ.draw (win)
	circ = Circle(Point(50, 20), 5)
	circ.setFill('purple')
	circ.draw (win)
	circ = Circle(Point(55, 30), 5)
	circ.setFill('purple')
	circ.draw (win)
	circ = Circle(Point(65, 35), 5)
	circ.setFill('purple')
	circ.draw (win)
	circ = Circle(Point(65, 25), 5)
	circ.setFill('purple')
	circ.draw (win)
	circ = Circle(Point(65, 15), 5)
	circ.setFill('purple')
	circ.draw (win)
	circ = Circle(Point(80, 35), 5)
	circ.setFill('white')
	circ.draw (win)
	circ = Circle(Point(85, 25), 5)
	circ.setFill('white')
	circ.draw (win)
	circ = Circle(Point(90, 15), 5)
	circ.setFill('white')
	circ.draw (win)
	circ = Circle(Point(95, 25), 3)
	circ.setFill('white')
	circ.draw (win)
	circ = Circle(Point(100, 15), 5)
	circ.setFill('white')
	circ.draw (win)
	circ = Circle(Point(105, 25), 5)
	circ.setFill('white')
	circ.draw (win)
	circ = Circle(Point(110, 35), 5)
	circ.setFill('white')
	circ.draw (win)
	circ = Circle(Point(5, 50), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(5, 60), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(5, 70), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(15, 70), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(35, 70), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(35, 60), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(35, 50), 3)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(60, 65), 10)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(80, 70), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(80, 60), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(80, 50), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(90, 60), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(100, 60), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(105, 70), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(120, 70), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(130, 65), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(125, 55), 5)
	circ.setFill('gray')
	circ.draw (win)
	circ = Circle(Point(135, 50), 5)
	circ.setFill('gray')
	circ.draw (win)
main()
input("Press the <Enter> key to quit.")

# A program that encodes a message.

def main(): 
  message = input("Enter the message to encode ")
  key = int(input("Enter the amount of the shift "))
  for ch in message:
    message = chr(ord(ch) + key)
    print (message, end = "")
main()

# A program asking someone how many people they have in their contacts.
 
def main():
	n = int(input("How many people are in your contact list? "))
	contacts = []
	for i in range(n):
		fname = (input("Enter the first name: "))
		lname = (input("Enter the last name: "))
		contact = str(i + 1) + ". " + lname + ", " + fname
		contacts.append(contact)
	for contact in contacts:
		print(contact)
main()

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

# last program of review

# This program converts liters to gallons 

print("The following is a converter of liters to gallons from 1 - 10") 

def main():
	for i in range(10): 
		liters = i + 1
		gallons = liters * 0.264172
		print(liters,"\t",gallons)
	input("Press the <Enter> key to quit.")
main()