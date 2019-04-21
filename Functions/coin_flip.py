from random import random

def flip_coin():
	# generate random number 0-1
	random_unmber = random()
	if random_unmber > 0.5:
		return "Heads"
	else:
		return "Tails"

print(flip_coin())
