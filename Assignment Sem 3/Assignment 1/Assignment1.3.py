# WAP: Length of String Using Function
def string_length(s):
    # print("Using ""len()"" function", len(s))
    length = 0
    for char in s:
        length += 1
    return length


text = input("Enter a string: ")
print("Length of the string is:", string_length(text))
