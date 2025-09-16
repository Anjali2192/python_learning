# ● ┌ ─ ┐ │ └ ┘
import random

def players():
    name = ("A", "B")
    player1 = random.choice(name)
    if player1 == "B":
        player2 = "A"
    else:
        player2 = "B"
    return player1, player2

board = [[" " for _ in range(3)] for _ in range(3)]
def print_board(board):
    for i,row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")
            
def win_p1():
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print(f"{p1} you won this game")
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print(f"{p1} you won this game")
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print(f"{p1} you won this game")
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print(f"{p1} you won this game")
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print(f"{p1} you won this game")
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print(f"{p1} you won this game")
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print(f"{p1} you won this game")
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print(f"{p1} you won this game")

def game(board):
    while True:
        row1 = int(input(f"{p1} which row you want to replace with X: "))
        column1 = int(input(f"{p1} which column you want to replace with X: "))
        board[row1][column1] = "X"
        print(print_board(board))

        row2 = int(input(f"{p2} which row you want to replace with O: "))
        column2 = int(input(f"{p2} which column you want to replace with O: "))
        board[row2][column2] = "O"
        print(print_board(board))

p1, p2 = players()

print(f"{p1} will start first!")

game(board)
