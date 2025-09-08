sntnc = input("Please enter any word: ")
word = {}
for i in sntnc:
    if i in word:
        word[i] += 1
    else:
        word[i] = 1

print(word)