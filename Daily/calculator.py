def add(num1, num2):
    print("The sum of ", num1, "+", num2, "is :", num1 + num2)


def sub(num1, num2):
    print("The subtraction of ", num1, "-", num2, "is :", num1 - num2)


def mul(num1, num2):
    print("The multiplication of ", num1, "*", num2, "is :", num1 * num2)


def div(num1, num2):
    print("The divition of ", num1, "/", num2, "is :{:.2f}".format(float(num1 / num2)))


num1 = int(input("Please enter a Number :"))
num2 = int(input("Please enter a Number :"))
inp = int(input("Menu\n1.Additon\n2.Subtraction\n3.Additon.\n4.Divition\nChoose:"))
if inp == 1:
    add(num1, num2)
elif inp == 2:
    sub(num1, num2)
elif inp == 3:
    mul(num1, num2)
elif inp == 4:
    div(num1, num2)
else:
    print("You chose the wrong answer!!")
