import datetime

date = int(input("Please enter the Date : "))
month = int(input("Please enter the Month : "))
year = datetime.datetime.now().year

x = datetime.datetime(year, month, date)

print(x.strftime("%A"), "of", year)
