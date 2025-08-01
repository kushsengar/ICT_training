word = input("Enter the word :")
n = len(word)
for ch in word[::-1]:
    print(ch, end=" ")