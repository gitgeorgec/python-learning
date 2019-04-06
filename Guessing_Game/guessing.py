import random

random_number = random.randint(1, 10)

while True:
	guess = int(input("Guess a number between 1 to 10: "))
	if guess > random_number:
		print("Too high, try again!")
	elif guess < random_number:
		print("Too low, try again!")
	else:
		print("You guessed it! You won")
		state = input("Do you want to keep playing? (y/n)")
		if(state == "y"):
			random_number = random.randint(1,10)
			guess = int(input("Guess a number between 1 to 10: "))
		elif(state == "n"):
			print("Thank you for playing!")
			break
