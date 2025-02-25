def call(num,num2):
    op=input("Please enter a operator (+,-,*,/): ")
    if op =="+":
        print(f"The Sum of {num} and {num2} : ",num+num2)
    elif op =="-":
        print(f"The Subtraction of {num} and {num2} : ",num-num2)
    elif op =="*":
        print(f"The Multiplication of {num} and {num2} : ",num*num2)
    elif op =="/":
        print(f"The Division of {num} and {num2} : ",num/num2)
    else:
        print("Please choose the correct operator")
        call(num,num2)

num=float(input("Please enter a number : "))
num2=float(input("Please enter a number : "))
call(num,num2)