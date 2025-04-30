n = int(input("Enter the value of N: "))
s = 0
for i in range(1,n+1):
    print(f"{i}^3:",pow(i,3))
    s = s + pow(i,3)
print(f"The sum of 1^3 + 2^3 + 3^3 + 4^3 + .......+ {n}^3 is :", s)
