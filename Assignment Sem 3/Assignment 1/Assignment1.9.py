# WAP: Sum of Odd Numbers from 1 to 10
total = 0

for i in range(1, 11):
    if i % 2 != 0:
        total += i

print("Sum of odd numbers from 1 to 10 is:", total)
