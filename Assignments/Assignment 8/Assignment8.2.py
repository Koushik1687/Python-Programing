text = input("Please enter the text : ")
file_name = input("Please enter the file name along with the file extension : ")

# file write
file = open(file_name, "a")
file.write(text)
file.close()

# display
file = open(file_name, "r")
print(file.read())
file.close()