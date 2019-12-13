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

def main2():
	try:
		numeric_grade = numeric_input()
		letter_grade = processing(numeric_grade)
		output(letter_grade)
	except:
		print("You must enter a number.")
main2()

# A program that encodes a message.

def main3(): 
  message = input("Enter the message to encode: ")
  key = int(input("Enter the amount of the shift: "))
  for ch in message:
    message = chr(ord(ch) + key)
    print (message, end = "")
main3()