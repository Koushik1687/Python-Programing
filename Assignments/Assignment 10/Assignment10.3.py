from datetime import date, timedelta
x = date.today()
d = int(input("Please enter days you want to subtract :"))
print(f"Current Date : {x}")
print(f"After subtraction the date {x - timedelta(d)}")