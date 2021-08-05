def main():
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the year: "))

    date1 = "{0}/{1}/{2}".format(month, day, year)

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    date2 = "{0} {1}, {2}".format(months[month-1],day,year)

    print("The date is {0} or {1}.".format(date1, date2))

main()

def dos():
    phrase = input("Enter a phrase: ")
    acronym = ""
    for word in phrase.split():
        acronym = acronym + word[0]
    acronym = acronym.upper()

    print("The acronym is", acronym)

dos()

def three():
    score = int(input("Between 0 - 100, enter the score: "))
    grades = 60*"F"+10*"D"+10*"C"+10*"B"+11*"A"
    print("The grade is", grades[score])

three()