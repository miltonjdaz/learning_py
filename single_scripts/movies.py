# Author: Milton D'az
# File: movies.py
#
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