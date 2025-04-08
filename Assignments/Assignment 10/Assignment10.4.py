path = "D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 10\\company_sales_data.csv"
with open(path, 'r') as f:
    line = f.readlines()
    lt = []
    for i in line:
        lt.append(i)
print(lt)