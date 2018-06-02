#combine 2 lits minus duplicates
a = ["Matt", "Bob", "Jill"]
b = ["Matt", "Sally", "Bob"]
c = []

for e in a:
	c.append(e)

for e in b:
	if e not in a:
		c.append(e)

for e in c:
	print(e)