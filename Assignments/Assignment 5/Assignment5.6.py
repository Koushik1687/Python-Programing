numbers = [10, 20, 4, 45, 99, 12, 7]
largest = max(numbers)
index = numbers.index(largest)
if index > 0:
    predecessor = numbers[index - 1]
else:
    predecessor = None
if index < len(numbers) - 1:
    successor = numbers[index + 1]
else:
    successor = None
print("Largest number:", largest)
print("Predecessor:", predecessor)
print("Successor:",successor)