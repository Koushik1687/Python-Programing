import numpy as np
def formula():
    x = int(input("Enter a number :"))
    y = int(input("Enter a number :"))
    z = int(input("Enter a number :"))
    pi = np.pi
    result = 4 * (x ** 4) + 3 * (y ** 3) + 9 * (z ** 2) + 6 * pi
    print("{:.2f}".format(result))

formula()
