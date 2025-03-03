numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
if len(numbers) >= 2:
    numbers[0] = int(input("Enter the new first element: "))
    numbers[-1] = int(input("Enter the new last element: "))
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)
print("Sorted list in ascending order:", ascending)
print("Sorted list in descending order:", descending)
