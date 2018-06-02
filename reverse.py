#return words in reverse order
a = input("string plz: ")
b = a.split()
c = []
for e in b:
	c.insert(0,e)
for e in c:
	print(e)