#right click white area, open in terminal, type code (Fill in blank).py

# Basic function
def hello(): 
    print("Hello World!")

hello()

# Basic parameter 

def greet(person):
    print("Hello", person)
    print("How are you?")

greet("Claire")

# A simple program illustrating chaotic behavior

def main(): 
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x* (1-x) 
        print(x)
main()