import math 

def sphereArea():
    r = int(input("What is the length of the radius: "))
    area = (4)*(math.pi)*(r^2)
    return area

def sphereVolume(): 
    r = int(input("What is the length of the radius: "))
    volume = (4/3)*(math.pi)*(r^3)
    return volume

def vanda(): 
    V = sphereVolume()
    A = sphereArea()
    print("The volume of the sphere is:", V)
    print("The surface area of the sphere is:", A)

vanda()

def calc():
    pounds = eval(input("How many pounds of coffee do you want: "))
    c = (10.50 * pounds) + (.86 * pounds) + 1.50
    return c

def main(): 
    cost = calc()
    print("The cost of your order is:", cost)

main()

def distance():
    sec = int(input("How many have seconds passed: "))
    sos = 1100 * sec
    miles = float(sos/5280)
    return miles

def light(): 
    m = distance()
    print("The number of miles from the lightning strike is:", m, "miles")

light()