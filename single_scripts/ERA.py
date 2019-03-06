# Author: Milton D'az
# File: ERA.py
#
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
