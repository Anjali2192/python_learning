import random
count = 1
low = 1
high = 100
number = random.randint(low,high)
print("******LET'S START******")
while True:
    guess = input("Guess the no choosen by computer b/w 1-100 : ")
    if guess == "q":
        break
    elif int(guess) == number:
        print("You got the number right!")
        print(f"You guessed it in {count} attempts")
    elif 1 < int(guess) < number:
        count += 1
        print("The actual no is greater than this")
    elif 100 > int(guess) > number:
        count += 1
        print("The actual no is smaller than this")
    else:
        print("Please Enter a valid number")