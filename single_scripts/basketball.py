# Author: Milton D'az
# Date: 2/15/2019
# File: basketball.py
#
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