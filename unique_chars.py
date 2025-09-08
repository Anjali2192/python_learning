sntnc = input("Please enter any word: ")
word = {}
for i in sntnc:
    if i in word:
        word[i] += 1
    else:
        word[i] = 1

print(word)

for key,value in word.items():
    if value != 1:
        print("All characters are not unique")
        break
    else:
        continue
    
else:
    print("All characters are unique")