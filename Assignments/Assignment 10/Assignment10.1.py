import os
file = input("Please enter the file name :")
if os.path.isfile(f"C:\\Koushik_Python\\{file}"):
    print("File is Present")
else :
    print("File is Not Present")