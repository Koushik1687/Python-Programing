# WAP: Single + Multiple Inheritance
class Animal:              # Single Inheritance
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Father:           #Multiple Inheritance
    def property(self):
        print("Father's property")

class Mother:
    def care(self):
        print("Mother's care")

class Child(Father, Mother):
    def show(self):
        print("Child enjoys both property and care")


print("=== Single Inheritance ===")
d = Dog()
d.sound()
d.bark()

print("\n=== Multiple Inheritance ===")
c = Child()
c.property()
c.care()
c.show()
