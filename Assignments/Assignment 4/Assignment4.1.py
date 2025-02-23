day = int(input("Enter day: "))
month = int(input("Enter month (1-12): "))
months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_year = sum(months_days[:month-1]) + day
print("Day of the year:", day_of_year)
