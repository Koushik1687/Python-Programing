with open("D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignmnet 7\\Assignmnet7.10_source.txt", "r") as source, open("D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignmnet 7\\Assignmnet7.10_destination.txt", "w") as destination:
    destination.write(source.read())

print("File copied successfully!")
