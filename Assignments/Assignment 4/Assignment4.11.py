List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Enter the number 1 to 10 to search: "))
count = List1.count(n)

if count > 0:
    print(f"The number {n} is present {count} time(s) in the list.")
else:
    print(f"The number {n} is not present in the list.")
    

