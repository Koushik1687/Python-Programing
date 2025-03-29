import mysql.connector
# to istall mysql use this -- #python -m pip install mysql-connector-python#

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  port="3306",
  database = 'python_atm'
)

cursor = mydb.cursor()

# Execute a query
cursor.execute("select * from passcode")

# Fetch and print results
rows = cursor.fetchall()

for row in rows:
  print(row)

num = int(input("Please enter new password : "))


cursor.execute(f"UPDATE passcode SET Passcode = {num} WHERE Cardno = 4526788496324592")
mydb.commit()
print()
print()
cursor.execute("select * from passcode")

# Fetch and print results
rows = cursor.fetchall()

for row in rows:
  print(row)
  
  
# Close connection
cursor.close()
mydb.close()