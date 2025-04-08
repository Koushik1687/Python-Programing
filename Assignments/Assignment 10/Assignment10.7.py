import csv
from matplotlib import pyplot as plt

path = "D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 10\\company_sales_data.csv"

with open(path, "r") as f:
    dict_data = csv.DictReader(f)
    dict_data.fieldnames = [field.strip() for field in dict_data.fieldnames]  # strip spaces

    monthNumber = []
    totalProfit = []
    for row in dict_data:
        monthNumber.append(int(row["month_number"]))
        totalProfit.append(float(row["total_profit"]))

plt.plot(monthNumber, totalProfit)
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.title("Company Sales Data")
plt.show()
