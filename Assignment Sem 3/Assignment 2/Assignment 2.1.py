#WAP: Max of 3 numbers using function
def max_number():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    return max(nums)

print("Maximum number is:", max_number())


def max_of_three(a, b, c):
    return max(a, b, c)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
#
# print("Maximum number is:", max_of_three(a, b, c))
