import random 

# array of possible moves 
move_list = ["Rock", "Paper", "Scissors"]

# our code to randomize the comuter's move 
def get_computer_move():
    rand = random.randint(0, 2)
    return move_list[rand]


# Players move 
user_move = input("Enter 'Rock', 'Paper', or 'Sicissors':\n")

# this declares the winner
def declare_winner(player, computer):
    # player and computer move as lowercase of first letter
    player_move = player[0].lower()
    computer_move = computer[0].lower()
    # make readability easier
    print("You played: ", player)
    print("Computer played: ", computer)
    # declare the winner 
    if player_move == computer_move:
        print("Tie Game!")
    elif player_move == "r" and computer_move == "s" or player_move == "p" and computer_move == "r" or player_move == "s" and computer_move == "p":
        print("YOU WIN!!!")
    else:
        print("YOU LOSE!!!")

declare_winner(user_move, get_computer_move())
