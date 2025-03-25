file=open("D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 8\\Assignment8.6.txt", 'r')
data=file.read()
for i in data:
    if i.isdigit():
        print(i)