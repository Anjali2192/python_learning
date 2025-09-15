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
def print_board():
    for i,row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")

#def game():
#    a = input(f"{p1} which box you want to replace with X(A-I): ").upper()
#    if a == "A":
#        print(board.box1)
#        b = input(f"{p2} which box you want to replace with O(A-I): ").upper() 

p1, p2 = players()
print(f"{p1} will start first!")
print(f"{p2} your's next turn!")

print_board()
#game()