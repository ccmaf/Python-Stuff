#take 2 lists and combine the like elements in another list
a = [1,2,3,4,5,99,11,14]
b = [1,2,3,4,5,101,13,18]
c = []

for element in a:
	if element in b:
		c.append(element)
for element in c:
	print(element)