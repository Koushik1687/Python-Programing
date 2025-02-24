List1 = [3, 7, 1, 9, 5, 10, 6]
largest = max(List1)
index = List1.index(largest)

predecessor = List1[index - 1] if index > 0 else None
successor = List1[index + 1] if index < len(List1) - 1 else None

print("Largest element:", largest)
print("Predecessor:", predecessor)
print("Successor:", successor)