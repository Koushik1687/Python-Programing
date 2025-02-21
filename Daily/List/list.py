l = [9,4,2,70,33,15,6,1,4,5,7]
l.sort(reverse=True)
l.append(45)
print(l)
print(l.index(1))
print(l.count(4))
m=[70,8,9,5,6,14,3,4,78,95,5]
m.insert(4,55)
print(m)
m[0] = 2
print(m)
k = m.copy()
print(k)