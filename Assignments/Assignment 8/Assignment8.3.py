file = open("D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 8\\Assignment8.3.txt",'r')
count = 0
for line in file:
    # print(line)
    count +=1
print(count)
file.close()