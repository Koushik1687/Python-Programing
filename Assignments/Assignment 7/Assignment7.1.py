num = int(input("Please enter the range : "))
odd =  1
count = 1
for i in range(num):
    count +=odd
    print(count, end=" ")
    odd +=2