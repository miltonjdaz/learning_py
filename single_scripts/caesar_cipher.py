# Author: Milton D'az
# Date: 2/18/2019
# File: caesar_cipher.py
#
# A program that encodes a message.

def main(): 
  message = input("Enter the message to encode ")
  key = int(input("Enter the amount of the shift "))
  for ch in message:
    message = chr(ord(ch) + key)
    print (message, end = "")
main()