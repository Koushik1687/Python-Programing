import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  port="3306",
  database = 'python_atm'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM PASSCODE")

for x in mycursor:
  # if x[1] == 4682:
  #   print("hello")
  print(x)


# data_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)
# mid = len(data_tuple) // 2
# first_half = data_tuple[:mid]
# second_half = data_tuple[mid:]
# print(f"First half: {first_half}")
# print(f"Second half: {second_half}")