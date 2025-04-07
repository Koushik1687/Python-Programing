num = int(input("Please enter number of line your want to print :"))
with open("D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 9\\Assignment9.1.txt","r") as f:
    fline= f.readlines()
    for line in fline[-num:]:
        print(line.strip())