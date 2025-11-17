# WAP: Basic Superclass & Subclass
class Animal:     # superclass
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):   # subclass
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()
