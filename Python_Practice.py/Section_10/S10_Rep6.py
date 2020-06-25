# Section 10 Rep 6
# A circular Button widget

from graphics import *

class CButton:

    """A button is a labeled circle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, radius, label):
        """ Creates a circular button, eg:
        qb = Button(myWin, Point(30,25), 20, 'Quit') """ 

        
        self.cx = center.getX()
        self.cy = center.getY()
        self.rsquare = radius * radius
        self.circle = Circle(center, radius)
        self.circle.setFill('lightgray')
        self.circle.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "RETURNS true if button active and p is inside"
        dx = p.getX() - self.cx
        dy = p.getY() - self.cy
        return self.active and dx*dx + dy*dy <= self.rsquare

    def getLabel(self):
        "RETURNS the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.circle.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = False