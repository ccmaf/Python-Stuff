#take a number from user input and list all its divisors
x = input("give me a positive integer: ")
list = range(1, int(x))
for element in list:
	if int(x) % element == 0:
		print(element)