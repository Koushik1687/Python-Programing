num1 = int(input("Please enter 1 numbers :"))
num2 = int(input("Please enter 2 numbers :"))
num3 = int(input("Please enter 3 numbers :"))

if num1 == num2 or num2 == num3 or num1 == num3:
    print("Numbers are not unique")
    if num1 == num2 and num2 == num3:
        print(f"Number 1: {num1} and Number 2: {num2} and Number 3: {num3} are all not unique")
    elif num1 == num2 :
        print(f"Number 1: {num1} and Number 2: {num2} are both not unique")
    elif num2 == num3:
        print(f"Number 2:{num2} and Number 3: {num3} are both not unique") 
    elif num1 == num3:
        print(f"Number 1:{num1} and Number 3: {num3} are both not unique") 
    
else:
    print("All numbers are unique")
