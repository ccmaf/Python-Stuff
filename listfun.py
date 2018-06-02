#goal: make a list from user input and print out any 
#number from the list that is < 5
print("please enter 3 numbers.")
n1 = input("n1: ")
n2 = input("n2: ")
n3 = input("n3: ")
list = [int(n1),int(n2),int(n3)]
for element in list:
	if element < 5:
		print(element)