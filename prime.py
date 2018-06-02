#ask user for a number and determine if it is prime
a = int(input("give me a number: "))
b = range(1, a)
c = 0

for element in b:
	if a % element == 0:
		c = c + element
if c == 1:
	print("the number is prime.")
else:
	print("the number is not prime.")
