#generate the fibonnaci sequence to n iterations
n = int(input("how many iterations?"))
f = [1,1]
if n == 1:
	print("1")
if n == 2:
	print("1")
	print("1")

while n > 2:
	f.append(f[len(f)-2] + f[len(f)-1])
	n = n-1
for element in f:
		print(element)