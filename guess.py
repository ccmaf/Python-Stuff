#create a random int and have the user try to guess it
import random
a = random.randint(1,9)
b = input("guess a number 1-9: ")
if a == int(b):
	print("that's right, the number is " + str(a) + "!")
else:
	print("WRONG! The number was " + str(a) + ".")