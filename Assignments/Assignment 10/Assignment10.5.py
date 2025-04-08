import csv
path = "D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 10\\company_sales_data.csv"
with open(path, 'r') as f:
    csv_reader = csv.DictReader(f)
    data_list = []
    for i in csv_reader:
        data_list.append(i)

for data in data_list:
    print(data)