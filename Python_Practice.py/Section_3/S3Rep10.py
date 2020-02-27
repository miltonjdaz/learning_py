""" Section 3 Rep 10 """

# Program to determine the length of a ladder 
import math 

def main(): 
    height = float(input("How high is the wall: "))
    angle = float(input("What will the ladder angle be (in degrees): "))

    radians = math.pi * angle / 180 
    length = height / math.sin(radians)

    print("Length of ladder required:", length)

main() 