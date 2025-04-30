employees = {"Koushik": 95000,"Subhranil": 120000,"Tiyasha": 105000,"Chandrima": 98000,"Arnab": 150000}
count = 0
for i in employees.values():
    if i >100000:
        count =+ count +1
print(f"Number of employees earning more than ₹1,00,000 per annum: {count}")