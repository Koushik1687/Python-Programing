def divisible(num1, num2):
    if num1 % num2 == 0:
        print("Fully Divisible :", num1 % num2)
    else:
        print("Not Fully Divisible : ", num1 % num2)


num1 = int(input("Enter a number :"))
num2 = int(input("Enter a number :"))
divisible(num1, num2)
