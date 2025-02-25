def calculate_income_tax(income):
    tax = 0
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = (250000 * 0.05) + (income - 500000) * 0.2
    else:
        tax = (250000 * 0.05) + (500000 * 0.2) + (income - 1000000) * 0.3
    return tax

income = float(input("Enter your annual income: "))
tax = calculate_income_tax(income)
print(f"Your income tax amount is: {tax:.2f}")
