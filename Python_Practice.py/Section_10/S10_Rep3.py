# Section 10 Rep 3 
# Extended Three Button Monte

from random import randrange
from graphics import *
from button import Button

def getDoorPick(win, b1, b2, b3):
    # waits for a click in b1, b2, or b3
    # returns the number of the door clicked
    choice = None
    while choice == None:
        pt = win.getMouse()
        for button in [b1, b2, b3]:
            if button.clicked(pt):
                choice = button
                    
    choiceNum = int(choice.getLabel()[-1])
    return choiceNum