with open("D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 7\\Assignment7.10_source.txt", "r") as source, open("D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 7\\Assignment7.10_destination.txt", "w") as destination:
    destination.write(source.read())

print("File copied successfully!")

# from docx  import Docunent