# Author: Milton D'az
# File: guess.py
#
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