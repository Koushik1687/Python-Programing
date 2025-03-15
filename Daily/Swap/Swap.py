lt = [1,2,3,4,5,6,8,9]
temp = 0
for i in range (len(lt)-1):
    temp = lt[i]
    lt[i] = lt[i+1]
    lt[i+1] = temp
print(lt)

