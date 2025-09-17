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

def win_p1(board):
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print(f"{p1} you won this game")
        return True
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print(f"{p1} you won this game")
        return True
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print(f"{p1} you won this game")
        return True
    elif board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        print(f"{p1} you won this game")
        return True
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        print(f"{p1} you won this game")
        return True
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        print(f"{p1} you won this game")
        return True
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print(f"{p1} you won this game")
        return True
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print(f"{p1} you won this game")
        return True

def win_p2(board):
    if board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        print(f"{p2} you won this game")
        return True
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        print(f"{p2} you won this game")
        return True
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print(f"{p2} you won this game")
        return True
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print(f"{p2} you won this game")
        return True
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        print(f"{p2} you won this game")
        return True
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        print(f"{p2} you won this game")
        return True
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print(f"{p2} you won this game")
        return True
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0]  == "O":
        print(f"{p2} you won this game")
        return True

def game(board):
    while True:
        row1 = int(input(f"{p1} which row you want to replace with X: "))
        column1 = int(input(f"{p1} which column you want to replace with X: "))
        board[row1][column1] = "X"
        print_board(board)
        if win_p1(board) is True:
            break
    
        row2 = int(input(f"{p2} which row you want to replace with O: "))
        column2 = int(input(f"{p2} which column you want to replace with O: "))
        board[row2][column2] = "O"
        print_board(board)
        if win_p2(board) is True:
            break

p1, p2 = players()

print(f"{p1} will start first!")

game(board)
