lt = []
c=0
while c < 3:
    num = int(input(f"Enter number {c} :"))
    if num not in lt:
        lt.append(num)
        c = c+1
print("max is : ",max(lt))
print("min is : ",min(lt))
