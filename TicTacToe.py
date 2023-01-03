board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
possible_moves = ["top left", "top middle", "top right", "middle left", "middle middle", "middle right", "bottom left", "bottom middle", "bottom right"]
player_one_turn = True
is_winner = False

# Adding players move to the board.
# Input move as a string
def add_move(move):
    words = move.split()
    if words[0] == "top":
        row = 0
    elif words[0] == "middle":
        row = 1
    else:
        row = 2
    if words[1] == "left":
        col = 0
    elif words[1] == "middle":
        col = 1
    else:
        col = 2
    if player_one_turn:
        board[row][col] = "X"
    else:
        board[row][col] = "O"


def user_input():
    # print possible moves to enter
    print("Possible moves are: ", possible_moves)
    if player_one_turn:
        user_move = input("Player one make your move: ")
    else:
        user_move = input("Player two make your move: ")
    if user_move in possible_moves:
        # add to board
        add_move(user_move)
        # remove from possible_moves
        possible_moves.remove(user_move)
        return possible_moves
    else:
        print("Move not valid")
        return user_input()  


def print_board():
    separator = "-----------"
    for row in range(len(board)):
        for col in range(len(board[row])):
            if col == len(board[row]) - 1:
                print(board[row][col])
            else:
                print(board[row][col], end=" | ")
        if row < len(board) - 1:
            print(separator)


# check if there is three in a row 
# output int 1 or 2 
# if no winner -1 
def check_winner():
    if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" or 
    board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" or 
    board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" or 
    board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" or
    board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" or
    board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X" or
    board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X" or
    board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        return 1
    elif (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" or 
    board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O" or 
    board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O" or
    board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O" or
    board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O" or
    board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O" or
    board[0][0] == "O" and board[1][1] == "o" and board[2][2] == "O" or
    board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        return 2
    else:
        return -1


def main():
    global player_one_turn
    global is_winner
    while len(possible_moves) > 0:
       user_input()
       print_board()
       # check for a winner and break if so
       winner = check_winner()
       if winner != -1:
            if winner == 1:
                print("PLAYER 1 WINS!!!!!")
            else:
                print("PLAYER 2 WINS!!!!!")
            is_winner = True
            break
       # change whose turn it is
       player_one_turn = not player_one_turn
    if not is_winner:
        print("CATS GAME :(")


# print_board(sample_board)
main()
