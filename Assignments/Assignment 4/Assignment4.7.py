num = int(input("Enter an integer number: "))
digits = [int(d) for d in str(abs(num))]

print("Sum of all digits:", sum(digits))
print("Largest digit:", max(digits))
print("Number of digits:", len(digits))
print("Difference between greatest and smallest digit:", max(digits) - min(digits))
print("Frequency of digits:", {d: digits.count(d) for d in set(digits)})