word = input()
sortWord = word
for i in range(1, len(word)):
    for j in range(i+1, len(word)):
        sortWord = min(sortWord, word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])
print(sortWord)