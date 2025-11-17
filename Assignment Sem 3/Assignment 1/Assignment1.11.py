# WAP: Add Item by Converting Tuple to List
t = (1, 2, 3)

temp = list(t)
temp.append(4)
t = tuple(temp)
print(t)
