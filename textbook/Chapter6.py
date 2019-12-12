# Using functions to sing Happy Birthday

def happy(): 
    print("Happy Birthday to you")

def sing(person): 
    happy()
    happy()
    print("Happy Birthday, dear", person + ".")
    happy()

def main(): 
    sing("Milton")
    print()
    sing("Claire")
    print()
    sing("Daisy")

main()

# 10 year investment modified
from graphics import *

def drawBar(window, year, height): 
    # draw a bar in window starting at year with given height
    bar = Rectanle(Point(year, 0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def main():
    # get principal and interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualizd interest rate: "))

    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1,0), ' 0.0k').draw(win)
    Text(Point(-1,2500), ' 2.5k').draw(win)
    Text(Point(-1,5000), ' 5.0k').draw(win)
    Text(Point(-1,7500), ' 7.5k').draw(win)
    Text(Point(-1,10000), '10.0k').draw(win)

    drawBar(win, 0, principal)
    for year in range(1,11): 
        principal = principal * (1 + apr)
        drawBar(win, year, principal)
    
    input("Press <Enter> to quit.")
    win.close()

main() 

# A modified version of happy birthday 

def happy2(): 
    return "Happy Birthday to you!\n"

def verseFor(person):
    lyrics = happy2()*2 + "Happy Birthday, dear " + person + ".\n" + happy2()
    return lyrics

def main2(): 
    for person in ["Milton", "Claire", "Daisy"]: 
        print(verseFor(person))

main2()

# A final version of the 10 year investment 

def createLabeledWindow():
    window = GraphWin("Investment Growth Chart", 320, 240)
    window.setBackground("white")
    window.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1,0), ' 0.0k').draw(window)
    Text(Point(-1,2500), ' 2.5k').draw(window)
    Text(Point(-1,5000), ' 5.0k').draw(window)
    Text(Point(-1,7500), ' 7.5k').draw(window)
    Text(Point(-1,10000), '10.0k').draw(window)
    return window

def drawBar(window, year, height): 
    # draw a bar in window starting at year with given height
    bar = Rectanle(Point(year, 0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def main2(): 
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualizd interest rate: "))

    win = createLabeledWindow()
    drawBar(win, 0, principal)
    for year in range(1,11):
        principal = principal * (1+apr)
        drawBar(win, year, principal)
    
    input("Press <Enter> to quit.")
    win.close()

main2()