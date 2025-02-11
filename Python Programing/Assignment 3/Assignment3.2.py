st1 = input("Please enter a string : ")
sub1 = input("Please enter :")
l = st1.split()
h = []
for x in l:
    for j in range(0, len(x)):
        h.append(x[j])
print(h)
count = 0
for x in h:
    if x == sub1:
        count += 1
print(count)
