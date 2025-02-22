import datetime

date = int(input("Please enter todays date : "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = datetime.datetime.now().month
year = datetime.datetime.now().year

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(29 - date, "Days left in this month")
else:
    print(days_in_month[month - 1] - date, "Days left in this month")
