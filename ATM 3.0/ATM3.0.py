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
            f"UPDATE passcode SET Passc ode = {confirm_pin} WHERE Passcode = {pin}"
        )
        mydb.commit()
        print("Your Pin has successfully updated")
        usermenu()
    else:
        print("Your pin dose't match")
        resetpin()


def usermenu():
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


def verify(pin,id):

    query.execute("select * from passcode")

    rows = query.fetchall()
    for row in rows:
        if row[1] == pin and row[3] == id:
            # print(row[1])
            # print(pin)
            print(f"\nHello {row[2]}, welcome to ABC Bank.")
            usermenu()
            break
    else:
        print("\nYou entered wrong pin.\nPlease try again !!\n")
        pin_enter()


def pin_enter():
    pin = int(input("Please Enter Your Pin : "))
    id = int(input("Please Enter Your Pin : "))
    verify(pin,id)


def createAccount():
    firstname = input("Please enter your First Name :")
    firstname = "'"+firstname+"'"
    middletname = input("Please enter your Middle Name :")
    middletname = "'"+middletname+"'"
    lastname = input("Please enter your Last Name :")
    lastname = "'"+lastname+"'"
    phoneno = int(input("Please enter your Phone Number :"))
    adharno = int(input("Please enter your Aadhar Number :"))
    panno = int(input("Please enter your Pan Number :"))
    h_f_num = input("Please enter your Flat/House Number :")
    h_f_num = "'"+h_f_num+"'"
  
    street = input("Please enter your Street :")
    street = "'"+street+"'"
    place = input("Please enter your Place :")
    place = "'"+place+"'"
    apincode = int(input("Please enter your Area Pincode :"))
    
    state = input("Please enter your State :")
    state = "'"+state+"'"
    country = input("Please enter your Country :") 
    country = "'"+country+"'"
  
    AccountNumber =2342697526
    query.execute("select * from passcode")

    rows = query.fetchall()
    for row in rows:
        if row[0] == AccountNumber:
            AccountNumber += AccountNumber
            if row[0] != AccountNumber:
                query.execute(f"INSERT INTO ACCOUNTS_DETAILS VALUES ({AccountNumber},{firstname},{middletname},{lastname},{phoneno},{adharno},{panno},{h_f_num},{street},{apincode},{place},{state},{country} );")
    else:
        print("\nYou entered wrong pin.\nPlease try again !!\n")
        pin_enter()
    
    mydb.commit()
    

def login():
  print("Welcome To ABC Bank \n")
  # time.sleep(2)
  op = int(input("Please chosse oprion below : \n 1.Creat Account \n 2.Generate Card Pin \n 3.Use ATM\nEnter your option :"))
  match op:
    case 1:
      createAccount()
    case 2: 
      print("Comming Soon")
    case 3:
      print("Please Insert Your Card")
      time.sleep(1)
      print("Please Wait We Are Reading Your Card's Chip")
      #time.sleep(1)
      pin_enter()    


login()
