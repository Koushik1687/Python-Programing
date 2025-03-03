employees = {"Koushik": 95000,"Subhranil": 120000,"Tiyasha": 105000,"Chandrima": 98000,"Arnab": 150000}
high_earners = sum(1 for salary in employees.values() if salary > 100000)
print(f"Number of employees earning more than ₹1,00,000 per annum: {high_earners}")
