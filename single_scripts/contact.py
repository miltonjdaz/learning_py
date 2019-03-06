# Author: Milton D'az
# File: contact.py
#
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