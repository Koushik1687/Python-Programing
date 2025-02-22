sen = input("Please enter a sentence : ").lower().split()
# print(len(sen))
vowel = ["a", "e", "i", "o", "u"]
print("Word\t\tVowels")
for words in sen:
    print(words, "\t",sum(1 for i in words if i in vowel))
