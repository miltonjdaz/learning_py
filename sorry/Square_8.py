# Figuring out GPA

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

def main():
    print("This program computes a student's GPA")
    student = Student("No Name", 0, 0)

    infoStr = input("Enter course info (gradepoints, credits): ")
    while infoStr != "":
        data = infoStr.split(",")
        gp, credits = float(data[0]), float(data[1])
        student.addGrade(gp, credits)
        infoStr = input("Enter course info (gradepoints, credits): ")

    print("\nSummary of courses entered:")
    print("hours:", student.getHours())
    print("GPA:", student.gpa())

main()

from random import randrange

def dos():
    print("This program estimates the probability of rolling")
    print("five of a kind on a single roll of 5 dice.\n")

    n = int(input("How many rolls should I simulate? "))
    hits = 0
    for i in range(n):
        if equalRolls(5):
            hits = hits + 1
    print("Estimated prob =", float(hits)/n)


def equalRolls(count):
    # count is number of dice to be rolled (must be >1)
    # returns True if all values turn out the same, False o/w
    first = randrange(1,7)
    for i in range(count-1):
        roll = randrange(1,7)
        if roll != first:
            return False
    # All rolls were equal to the first
    return True

dos()