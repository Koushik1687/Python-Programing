def calculate_income_tax(income):
    tax = 0
    
    if income <= 700000:
        tax = 0 
    elif income <= 1000000:
        tax = (income - 700000) * 0.1 
    elif income <= 1200000:
        tax = (300000 * 0.1) + (income - 1000000) * 0.2  
    elif income <= 1500000:
        tax = (300000 * 0.1) + (200000 * 0.2) + (income - 1200000) * 0.3 
    else:
        tax = (300000 * 0.1) + (200000 * 0.2) + (300000 * 0.3) + (income - 1500000) * 0.3  
    
    return tax

income = float(input("Enter your annual income: "))
tax = calculate_income_tax(income)
print(f"Your income tax amount is: {tax:.2f}")

