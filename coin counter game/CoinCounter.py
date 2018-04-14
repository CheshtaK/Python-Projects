import random

heads = 0
tails = 0
sides = 0

for i in range(0,100):
    flip = random.randint(0, 2)

    if flip == 0:
        heads += 1
    elif flip == 1:
        tails += 1
    else:
        sides += 1

print("Heads count %i" % heads)
print("Tails count %i" % tails)
print("Sides count %i" % sides)