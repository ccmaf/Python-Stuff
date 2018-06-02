#compare 2 lists and print common elements
a = [6, 3, 23, 24, 51, 99, 241]
b = [3, 4, 6, 19, 51, 123, 99]

for element in a:
	if element in b:
		print(element)