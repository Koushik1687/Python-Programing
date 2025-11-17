# WAP: Reverse a string using slicing
def reverse(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev
#     return s[::-1]

text = input("Enter a string: ")
print("Reversed string:", reverse(text))
