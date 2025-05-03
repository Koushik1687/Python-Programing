numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
if len(numbers) >= 2:
    numbers[0] = int(input("Enter the new first element: "))
    numbers[-1] = int(input("Enter the new last element: "))

print("Sorted list in ascending order:", sorted(numbers))
print("Sorted list in descending order:", sorted(numbers, reverse=True))
