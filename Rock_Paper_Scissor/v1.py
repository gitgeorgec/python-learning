player1 = input("enter player 1's choice: ")
player2 = input("enter player 1's choice: ")

print("Rock...")
print("Paper...")
print("Scissors...")
print("SHOOT")
if player1 == "rock" and player2 == "scissors":
    print("player1 wins")
elif player1 == "paper" and player2 == "rock":
    print("player1 wins")
elif player1 == "scissors" and player2 == "paper":
    print("player1 wins")
elif player2 == "rock" and player1 == "scissors":
    print("player2 wins")
elif player2 == "paper" and player1 == "rock":
    print("player2 wins")
elif player2 == "scissors" and player1 == "paper":
    print("player2 wins")
if player1 == player2 :
    print("it's a tie!")
else:
    print("somting is wrong!")
  