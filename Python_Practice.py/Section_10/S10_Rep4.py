# Section 10 Rep 4 
# Program to figure out a student's GPA

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

    def gpa(self):
        return self.qpoints/self.hours