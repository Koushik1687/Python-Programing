num = int(input("Enter an integer number: "))
digits = [int(d) for d in str(abs(num))]
print(digits)

print("Greatest  digit:", max(digits))
print("Smallest  of digits:", min(digits))
