# num = int(input("Please enter numbers : "))

# n1 = num//100
# print(n1)
# n2 = (num//10)%10
# print(n2)
# n3 = num%10
# print(n3)
# print(n3*100+n2*10+n1)

# class Car:
#     def __init__(self, make, model):  # Correct constructor
#         self.make = make
#         self.model = model

#     def car_info(self):
#         print(f"This is a {self.make} {self.model}.")

# car1 = Car("Toyota", "Corolla")
# car2 = Car("Honda", "Civic")

# car1.car_info()  # Output: This is a Toyota Corolla.
# car2.car_info()  # Output: This is a Honda Civic.


class Car:
    def __init__(self, company, name):
        self.company = company
        self.name = name

    def show(self):
        print("This is a", self.company, self.name)

# Create two car objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Show car details
car1.show()
car2.show()