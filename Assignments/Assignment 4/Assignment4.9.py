lt = [0,0,0,0,0,0]
l = ["Bengali","English","Mathematis","Science","History","Geography"]
for i in range(0,6):
    print("Please enter",l[i],"'s Makrs :")
    lt[i] = int(input())
sum = 0
print("\nThe marks you got: ")
for i in range(0,6):
    print(l[i],"Makrs :",lt[i])
    sum +=lt[i]
print()
print("The Maximum makrs :",max(lt))
print("The Minimum makrs :",min(lt))

print("The total Marks obtain is :",sum)