import os
file = input("Please enter the file name :")
if os.path.isfile(f"D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 10\\{file}"):
    print("File is Present")
else :
    print("File is Not Present")