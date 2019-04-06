import random
player_wins = 0
computer_wins = 0
winning_score = 5

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    computer = random.randint(0,2)
    if computer == 0:
        player2 = "rock"
    elif computer == 1:
        player2 = "paper"
    else:
        player2 = "scissors"

    player1 = input("enter player 1's choice: ").lower()
    if player1 == "quit":
        break

    print("computer choice: " + player2)
    if player1 == "rock" and player2 == "scissors":
        print("player1 wins")
        player_wins += 1
    elif player1 == "paper" and player2 == "rock":
        print("player1 wins")
        player_wins += 1
    elif player1 == "scissors" and player2 == "paper":
        print("player1 wins")
        player_wins += 1
    elif player2 == "rock" and player1 == "scissors":
        print("computer wins")
        computer_wins += 1
    elif player2 == "paper" and player1 == "rock":
        print("computer wins")
        computer_wins += 1
    elif player2 == "scissors" and player1 == "paper":
        print("computer wins")
        computer_wins += 1
    elif player1 == player2 :
        print("it's a tie!")
    else:
        print("somting is wrong!")
