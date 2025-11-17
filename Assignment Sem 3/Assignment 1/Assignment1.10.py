# WAP: Fibonacci Series Using for Loop
n = int(input("Enter how many terms: "))

a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b
