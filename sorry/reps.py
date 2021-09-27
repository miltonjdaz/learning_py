def main():
    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3.0 

    print(average)

main()

def dos():
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature: "))
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print()

dos()