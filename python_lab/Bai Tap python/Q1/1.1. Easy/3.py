# Create a list of 10 random numbers.
import random


ls = []
while len(ls) < 10:

    n = random.randint(0,100)
    ls.append(str(n))


print(f'{' '.join(ls)}')