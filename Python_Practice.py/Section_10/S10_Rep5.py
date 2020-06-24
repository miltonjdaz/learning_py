# Section 10 Rep 5
# Upgraded GPA 

import string

class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def addGrade(self, gradePoint, credits):
        self.qpoints = self.qpoints + gradePoint * credits
        self.hours = self.hours + credits

    def addLetterGrade(self, grade, credits):
        letter = grade[0].upper()
        plusminus = grade[1:].strip()
        if letter == 'A':
            score = 4.0
        elif letter == 'B':
            score = 3.0
        elif letter == 'C':
            score = 2.0
        elif letter == 'D':
            score = 1.0
        else:
            score = 0.0
        if plusminus == '+':
            score = score + .33
        elif plusminus == '-':
            score = score - .33
        self.qpoints = self.qpoints + score * credits
        self.hours = self.hours + credits

    def gpa(self):
        return self.qpoints/self.hours