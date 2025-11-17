# WAP: Add Member in a Set
def add_member(s, value):
    s.add(value)
    return s

my_set = {1, 2, 3}
print("This is the actual set :",my_set)
val = int(input("Enter a number to add in the set: "))
updated_set = add_member(my_set, 4)
print("This is the updated set :",updated_set)
