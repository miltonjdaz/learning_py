# Author: Milton D'az
# File: reverse_file.py
#
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