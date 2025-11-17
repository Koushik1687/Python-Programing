# WAP: Check if Given Key Already Exists in Dictionary
my_dict = {"name": "Ram", "age": 25, "city": "Kolkata"}

key = input("Enter key to check: ")

if key in my_dict:
    print("Key is already present")
else:
    print("Key is not present")
