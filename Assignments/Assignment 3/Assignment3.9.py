word = input("Enter a word: ").upper()
n = len(word)
for i in range(n):
    print((word[i] + " ") * (i + 1))
print()
for i in range(n):
    print(" ".join(word[: n - i]))
print()
