#Rock Paper Sissors!
a = input("P1: rock, paper, or sissors? ")
b = input("P2: rock, paper, or sissors? ")

if a == b:
	print("tie")
elif a == "rock":
	if b == "sissors":
		print("P1 wins!")
	else:
		print("P2 wins!")
elif a == "sissors":
	if b == "rock":
		print("P2 wins")
	else:
		print("P1 wins")
elif a == "paper":
	if b == "rock":
		print("P1 wins")
	else:
		print("P2 wins")
else:
	print("invalid input")
