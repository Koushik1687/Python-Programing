import re
from collections import Counter

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [file.readline().strip() for _ in range(100)]

    words = [word for line in lines for word in re.findall(r'\b\w+\b', line)]
    word_frequency = Counter(words)
    numbers = [word for word in words if word.isdigit()]
    hashtags = [word for word in words if word.startswith('#')]
    annotations = [word for word in words if word.startswith('@')]

    print(f"Distinct words: {list(set(words))[:10]} ...")   
    print(f"Word frequencies: {dict(list(word_frequency.items())[:10])} ...")
    print(f"Numbers: {numbers}")
    print(f"Hashtags: {hashtags}")
    print(f"Annotations: {annotations}")

process_file("Python\\Python-Programing\\Assignments\\Assignment 9\\Assignment9.1.txt")