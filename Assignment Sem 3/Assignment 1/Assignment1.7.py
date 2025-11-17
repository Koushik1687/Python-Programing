# WAP: Python program to check whether the input is a number or a character.
def check_input(x):
    if x.isdigit():
        return "Number"
    elif x.isalpha():
        return "Character"
    else:
        return "Special Symbol"

val = input("Enter something: ")
print("It is a", check_input(val))
