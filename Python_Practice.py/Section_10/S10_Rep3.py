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

def updateScore(choice, msg, score, hits, misses):
    # Compares choice to a random number
    # Displays win or loss in msg
    # Updates hits or misses and display of score
    # Returns updated hits and misses
    secret = randrange(1,4)
    tallyStr = "Wins: {0:2}   Losses: {1:2}"
    if choice == secret:
        msg.setText("You win!")
        hits = hits + 1
    else:
        msg.setText("You lose. The answer was door {0}.".format(secret))
        misses = misses + 1
    score.setText(tallyStr.format(hits,misses))
    return hits, misses