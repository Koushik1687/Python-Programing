odd = open("D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 8\\Assignment8.7_odd.txt",'w')
even = open("D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 8\\Assignment8.7_even.txt",'w')

num =  int(input("Enter the number of elements you want to enter :  "))

for i in range(1,num):
    if (i%2)==0:
        odd.write(str(i)+"\n")
    else:
        even.write(str(i)+"\n")
        
odd.close()
even.close()