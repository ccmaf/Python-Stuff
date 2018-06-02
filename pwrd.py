#Random password generator
import string
import random

a = string.ascii_letters + string.digits + string.punctuation

b = int(input("how many characters long should the password be? "))

c = "".join(random.sample(a, b ))

print(c)