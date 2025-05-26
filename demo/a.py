# Open and read the file
with open("sample.txt", "r") as file:
    text = file.read().lower()

# Split text into words
words = text.split()

# Count each word
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Find the most frequent word
most_common_word = max(word_count, key=word_count.get)

# Print results
print("Total words:", len(words))
print("Most frequent word:", most_common_word)
print("Occurrences:", word_count[most_common_word])
