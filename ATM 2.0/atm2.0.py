import time

def login():
    # print("Welcome To ABC Bank \nPlease Insert Your Card")
    # time.sleep(2)
    # print("Please Wait We Are Reading Your Card's Chip")
    # time.sleep(1)
    # pin = int(input("Please Enter Your Pin : "))
    verify()
    
def verify():
    i = 1
    passcode = open("D:\\Coding\\Python\\Python-Programing\\ATM 2.0\\passcode.csv",'r')
    for line in passcode:
        line = line.strip()
        print(line)
        line = line.split(',')
        print(line)
#         if i>0: 
#             if int(line[1])== ' ':
#                 print(line)
login()