player1 = input("enter player 1's choice: ")
player2 = input("enter player 1's choice: ")

print("Rock...")
print("Paper...")
print("Scissors...")
print("SHOOT")

if player1 == player2 :
    print("it's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("player1 wins")
    elif player2 == "paper":
        print("player2 wins")
elif player1 == "paper":
    if player2 == "rock":
        print("player1 wins")
    elif player2 == "scissors":
        print("player2 wins")
elif player1 == "scissors":
    if player2 == "paper":
        print("player1 wins")
    elif player2 == "rock":
        print("player2 wins")
else:
    print("somting is wrong!")
  