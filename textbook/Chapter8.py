# This program finds the average of numbers put in by the user

def main():
    n = int(input("How many numbers do you have? "))
    total = 0.0 
    for i in range(n): 
        x = float(input("Enter a number >> "))
        total = total + x 
    print("\nThe average of the numbers is", total / n)

main()

def more():
    total = 0.0
    count = 0 
    moredata = "yes"

    while moredata[0] == "y": 
        x = float(input("Enter a number >>"))
        total = total + x 
        count = count + 1 
        moredata = input("Do you have more numbers (yes or no)? ")
    print("\nThe average of the numbers is", total / count)

more()

def neg(): 
    total = 0.0
    count = 0 
    x = float(input("Enter a number (negative to quit) >> "))
    while x >= 0: 
        total = total + x 
        count = count + 1 
        x = float(input("Enter a number (negative to quit) >> "))
    print("\nThe average of the numbers is", total / count)

neg() 

def enter1(): 
    total = 0.0
    count = 0 
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "": 
        x = float(xStr)
        total = total + x 
        count = count + 1 
        x = input("Enter a number (<Enter> to quit) >> ")
    print("\nThe average of the numbers is", total / count)

enter1()

def fn(): 
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r')
    total = 0.0
    count = 0 
    for line in infile: 
        total = total + float(line)
        count = count + 1 
    print("\nThe average of the numbers is", total / count)

fn() 

def mainsix():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r')
    total = 0.0
    count = 0 
    line = infile.readline()
    while line != "":
        total = total + float(line)
        count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is", total / count)

mainsix()

def mainsev():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r')
    total = 0.0
    count = 0 
    line = infile.readline()
    while line != "":
        # update total and count for values in line
        for xStr in line.split(","):
            total = total + float(xStr)
            count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is" , total / count)

mainsev() 

# keyboard driven color changing window

from graphics import * 

def color():
    win = GraphWin("Color Window", 500, 500)
    # event loop: handle key presses until user presses the "q" key. 
    while True:
        key = win.getKey()
        if key == "q": # loop exit
            break
        # process the key 
        if key == "r": 
            win.setBackground("pink")
        elif key == "w":
            win.setBackground("white")
        elif key = "g": 
            win.setBackground("lightgray")
        elif key == "b":
            win.setBackground("lightblue")

    # exit program
    win.close()

color() 

from graphics import * 

def handleKey(k, win):
    if k == "r":
        win.setBackground("pink")
    elif k == "w": 
        win.setBackground("white")
    elif k == "g": 
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")

def handleClick(pt, win): 
    pass

def mainf():
    win = GraphWin("Click and Type", 500, 500)

    # event key: handle key presses and mouse clicks until the user presses the "q" key

    while True: 
        key = win.checkKey()
        if key == "q": # exit loop
            break 
        if key: 
            handleKey(key, win)
        pt = win.checkMouse()
        if pt: 
            handleClick(pt, win)
    win.close()

mainf() 