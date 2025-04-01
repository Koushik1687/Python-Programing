import re
from collections import Counter
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    cleaned_lines = [line.strip() for line in lines]
    
    words = [word for line in cleaned_lines for word in re.findall(r'\b\w+\b', line)]
    longest_words = sorted(set(words), key=len, reverse=True)[:10]
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(" ".join(cleaned_lines))
    print(f"Longest words: {longest_words}")
    print("Last Line:", cleaned_lines[-1])
process_file("Python\\Python-Programing\\Assignments\\Assignment 9\\Assignment9.1.txt")