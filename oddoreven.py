num = input("Give me a number: ")
if int(num) % 2 == 0:
	if int(num) % 4 == 0:
		print ("the number " + num + " is even and a multiple of 4")
	else:
		print ("the number " + num + " is even")
else:
	print ("the number " + num + " is odd")
