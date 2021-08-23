# My birthday is coming up 

def happy():
    print("Happy birthday to you")

def sing(person):
    happy()
    happy()
    print("Happy birthday, dear", person + ".")
    happy()

def main():
    sing("Milton")

main()

def eieio():
    return "Ee-igh, Ee-igh, Oh!"

def refrain():
    print("Old MacDonald had a farm,", eieio())

def hada(animal):
    print("And on that farm he had a", animal+",", eieio())

def witha(noise):
    noisecomma = noise + ","
    noise2 = noisecomma + " "+noise
    print("With a", noise2, "here and a", noise2, "there.")
    print("Here a", noisecomma, "there a", noisecomma, \
        "everywhere a", noise2+".")

def verse(animal, noise):
    refrain()
    hada(animal)
    witha(noise)
    refrain()

def dos():
    for a,n in [("cow","moo"), ("pig", "oink"), ("hedgehog", "Dinsdale")]:
        verse(a,n)
        print()

dos()