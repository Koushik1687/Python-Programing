at = []
bt = []
ct = []
wt = []
tat = []
num = int(input("Please enter the no. of processes :"))

print("Please enter Arriving Time :")
for i in range(1,num+1):
    a = int(input(f"Please enter {i} no. arriving :"))
    at.append(a)


print("Please enter Burst Time :")
for i in range(1,num+1):
    a = int(input(f"Please enter {i} no. burst :"))
    bt.append(a)

print(at)