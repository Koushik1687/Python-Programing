num = int(input("Please enter a number : "))
n = int(input("Please the rang of sqr : "))
for i in range(2,n+1):
    print(f"{num}^{i} =",pow(num,i))
