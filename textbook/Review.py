# A program asking someone how many numbers they want to average.
 
def main():
	n = int(input("How many numbers do you want to add? "))
	sum = 0 
	for i in range(n):
		value = int(input("Enter next num: "))
		sum = sum + value
		average = round(sum/n, 2)
	print()
	print(average)

main()

# A program that de-codes a message.

def main():
    encodemsg = input("Enter the message to decrypt: ")
    shift = int(input("Enter the amount of the shift: "))

    encodemsg = encodemsg.split()
    sentence = []

    for word in encodemsg:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o - shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        sentence.append(plaintext)
    sentence = ' '.join(sentence)
    print (sentence)
main()