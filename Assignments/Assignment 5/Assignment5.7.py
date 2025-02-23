emp_details = {}
while True:
    name = input("Please enter your Name : ")
    salary = float(input("Please enter your Salary : "))
    emp_details[name] = salary
    
    option = input("Do you want to add more data ? (yes/no): ").strip().lower()
    if option != 'yes':
        break
for name, salary in emp_details.items():
    print(f"{name}: {salary}")
