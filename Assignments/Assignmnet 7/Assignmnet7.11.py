upper = lower = 0

with open("D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignmnet 7\\Assignmnet7.11.txt", "r") as file:
    for line in file:
        print(line.strip())  
        for char in line:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
                
print("\nUppercase:", upper)
print("Lowercase:", lower)
