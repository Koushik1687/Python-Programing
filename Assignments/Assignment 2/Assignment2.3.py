sun = int(input("Enter the temperature of Sunday : "))
mon = int(input("Enter the temperature of Monday : "))
tue = int(input("Enter the temperature of Tuesday : "))
wed = int(input("Enter the temperature of Wednesday : "))
thue = int(input("Enter the temperature of Thursday : "))
fri = int(input("Enter the temperature of Friday : "))
sat = int(input("Enter the temperature of Saturday : "))
avg = (sun+mon+tue+wed+thue+fri+sat)/7
print("The average temperature of the week is ", round(avg, 2))
