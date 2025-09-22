import random

def players():
    A = input("Enter your name: ").capitalize()
    B = input("Enter other player's name: ").capitalize()
    name = (A, B)
    player1 = random.choice(name)
    if player1 == B:
        player2 = A
    else:
        player2 = B
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

def draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def row_column(box):
    if box == "A":
        row = 0
        column = 0   
    elif box == "B":
        row = 0
        column = 1
    elif box == "C":
        row = 0
        column = 2
    elif box == "D":
        row = 1
        column = 0
    elif box == "E":
        row = 1
        column = 1
    elif box == "F":
        row = 1
        column = 2
    elif box == "G":
        row = 2
        column = 0
    elif box == "H":
        row = 2
        column = 1
    elif box == "I":
        row = 2
        column = 2
    return row, column

def game(board):
    while True:
        box = input(f"{p1} which box you want to replace with X(A-I): ").capitalize()
        row, column = row_column(box)
        board[row][column] = "X"
        print_board(board)
        if win_p1(board) is True:
            break
        if draw(board) is True:
            print("The game is a draw")
            break
    
        box = input(f"{p2} which box you want to replace with O(A-I): ").capitalize()
        row, column = row_column(box)
        board[row][column] = "O"
        print_board(board)
        if win_p2(board) is True:
            break  
        if draw(board) is True:
            break

print("*******LET'S START*******")
p1, p2 = players()

print()
start_box = ["A | B | C",
             "--+---+--",
             "D | E | F",
             "--+---+--",
             "G | H | I"
             ]

for line in start_box:
    print(line)

print()
print(f"{p1} will start first!")
print()

game(board)
