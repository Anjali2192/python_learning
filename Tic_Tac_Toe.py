# ● ┌ ─ ┐ │ └ ┘
import random
box = [" A │ B │ C ",  
       "───│───│───", 
       " D │ E │ F ",  
       "───│───│───",  
       " G │ H │ I "
    ]

def players():
    name = ("A", "B")
    player1 = random.choice(name)
    if player1 == "B":
        player2 = "A"
    else:
        player2 = "B"
    return player1, player2

def board():
    for line in box:
        print(line)

p1, p2 = players()
print(f"{p1} will start first!")
print(f"{p2} your's next turn!")
board()