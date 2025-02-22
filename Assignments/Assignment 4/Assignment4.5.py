lst = []
for i in range(0,21):
    if i % 2 != 0:
        lst.append(i)
print(sorted(lst,reverse=True))
