#WAP: Representing a Superclass
class Vehicle:
    def show(self):
        print("This is a vehicle.")

# Subclass
class Car(Vehicle):
    def display(self):
        print("This is a car.")

# Main Code
c = Car()
c.show()
c.display()
