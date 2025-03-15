def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

with open("D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignmnet 7\\Assignmnet7.11.txt", "r") as file:
    for line in file:
        words = line.strip().split()  
        for word in words:
            print(f"{word}: {count_vowels(word)}")
