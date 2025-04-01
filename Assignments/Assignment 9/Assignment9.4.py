import re
from collections import Counter

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    words = [word for line in lines for word in re.findall(r'\b\w+\b', line)]
    longest_words = sorted(set(words), key=len, reverse=True)[:10]

    print(f"Longest words: {longest_words}")
    print("Last Line:", lines[-1].strip())

# Example usage:
process_file("Python\\Python-Programing\\Assignments\\Assignment 9\\Assignment9.1.txt")
