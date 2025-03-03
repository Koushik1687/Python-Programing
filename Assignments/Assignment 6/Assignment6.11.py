import random
import statistics
random_numbers = random.sample(range(10, 50, 5), 6)
mean_value = statistics.mean(random_numbers)
median_value = statistics.median(random_numbers)
mode_value = statistics.mode(random_numbers)
print("Generated numbers:", random_numbers)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
