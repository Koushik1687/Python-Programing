str = input("Enter a string: ")
upper = sum(1 for char in str if char.isupper())
lower = sum(1 for char in str if char.islower())

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
