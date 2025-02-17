import statistics

marks = list(map(int, input("Enter marks separated by spaces: ").split()))

print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))
print("Mode:", statistics.mode(marks))
