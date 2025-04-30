num = int(input("Please enter numbers : "))

n1 = num//100
n2 = (num//10)%10
n3 = num%10
print(n3*100+n2*10+n1)