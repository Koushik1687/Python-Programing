import time

def menu():
    op = int(input("\nChoose Any Option Below !!\n 1. Send Money \n 2. Transaction History \n 3. Rest Pin \n 4. Add Fund\n 5. Back\n\nEnter Your Option : "))
    if op == 3:
        i = 1
        passcode = open("D:\\Coding\\Python\\Python-Programing\\ATM 2.0\\passcode.csv", "r")
        pin = int(input("Please enter your old pin : "))
        for line in passcode:
            line = line.strip()
            data = line.split(',')
            if i>1:
                if int(data[1]) == pin:
                    passcode.close()
                    passcode = open("D:\\Coding\\Python\\Python-Programing\\ATM 2.0\\passcode.csv", "w")
                    # newpin = int(input("Please enter your new pin : "))
                    # int(data[1])==newpin
                    print(data)
            i = i+1
        
        

def display_data(data):
    time.sleep(1)
    print(f"Hello,{data[2]}. Welcome to ABC bank")
    menu()
    

def verify(pin):
    i = 1
    passcode = open("D:\\Coding\\Python\\Python-Programing\\ATM 2.0\\passcode.csv", "r")
    for line in passcode:
        line = line.strip()
        data = line.split(',')
        if i>1:
            if int(data[1]) == pin:
                print("Please Wait We Are Verifying...")
                display_data(data)
        i = i+1


def login():
    print("Welcome To ABC Bank \nPlease Insert Your Card")
    time.sleep(2)
    print("Please Wait We Are Reading Your Card's Chip")
    time.sleep(1)
    pin = int(input("Please Enter Your Pin : "))
    verify(pin)


login()
