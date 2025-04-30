lt = []
l = ["Bengali","English","Mathematics","Science","History","Geography"]
for i in range(0,6):
    print("Please enter",l[i],"'s Marks :")
    lt.append(int(input()))
print("\nThe marks you got: ")
for i in range(6):
    print(l[i],"Makrs :",lt[i])

print()  
print("The Maximum makrs :",max(lt))
print("The Minimum makrs :",min(lt))
print("The total Marks obtained is :",sum(lt))