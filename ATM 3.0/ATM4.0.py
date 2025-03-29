# to istall mysql use this -- #python -m pip install mysql-connector-python#
# host="localhost", user="root", password="root", database = 'python_atm, 'port="3306"

import mysql.connector
import time


mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="root", 
    port="3306", 
    database="python_atm"
)
query = mydb.cursor()


def resetpin():
    pin = int(input("Please enter your old pin : "))
    new_pin = int(input("Please enter your New pin : "))
    if pin == new_pin:
        print("Please choose other pin.")
        resetpin()
    confirm_pin = int(input("Please confirm your New pin : "))
    if new_pin == confirm_pin:
        query.execute(
            f"UPDATE passcode SET Passcode = {confirm_pin} WHERE Passcode = {pin}"
        )
        mydb.commit()
        print("Your Pin has successfully updated")
        menu()
    else:
        print("Your pin dose't match")
        resetpin()


def menu():
    op = int(
        input(
            "\nChoose Any Option Below !!\n 1. Send Money \n 2. Transaction History \n 3. Rest Pin \n 4. Add Fund\n 5. Back\n\nEnter Your Option : "
        )
    )
    if op == 1:
        print("Send Money Coming Soon")
    elif op == 2:
        print("Transaction History Coming Soon")
    elif op == 3:
        resetpin()
    elif op == 4:
        print("Add Fund Coming Soon")
    else:
        print("Thank You for chosing ABC Bank's ATM. Visit Again !! \n")
        time.sleep(1)
        login()


def verify(pin):
    query = mydb.cursor()
    query.execute("select * from passcode")

    rows = query.fetchall()
    for row in rows:
        if row[1] == pin:
            # print(row[1])
            # print(pin)
            print(f"\nHello {row[2]}, welcome to ABC Bank.")
            menu()
            break
    else:
        print("\nYou entered wrong pin.\nPlease try again !!\n")
        pin_enter()


def pin_enter():
    pin = int(input("Please Enter Your Pin : "))
    verify(pin)


def login():
    print("Welcome To ABC Bank \nPlease Insert Your Card")
    # time.sleep(2)
    print("Please Wait We Are Reading Your Card's Chip")
    # time.sleep(1)
    pin_enter()


login()
