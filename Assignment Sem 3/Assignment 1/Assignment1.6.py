# WAP: Python program to check whether a number is even or odd.
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print("The number is", even_or_odd(number))
