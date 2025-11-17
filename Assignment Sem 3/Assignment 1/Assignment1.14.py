# WAP: Largest Number From a List
def largest_num(lst):
    big = lst[0]
    for num in lst:
        if num > big:
            big = num
    return big

numbers = [10, 25, 7, 88, 3]
print("Largest number is:", largest_num(numbers))
