# WAP: Encapsulation
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    # getter methods
    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    # setter methods
    def set_marks(self, marks):
        self.__marks = marks

# Main Code
s = Student("Koushik", 85)

print("Name:", s.get_name())
print("Marks:", s.get_marks())

s.set_marks(95)
print("Updated Marks:", s.get_marks())
