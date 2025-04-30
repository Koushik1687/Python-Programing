str = input("Enter a string: ")
upper = 0
lower = 0

for i in str:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
