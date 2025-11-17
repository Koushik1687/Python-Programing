# WAP: Travelling Salesman Problem
from sys import maxsize
from itertools import permutations
v = 4
def tsp(graph, s):
    vertex = []
    for i in range(v):
        if i != s:
            vertex.append(i)
    min_path = maxsize
    next_permutations = permutations(vertex)
    for i in next_permutations:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)
    return min_path
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
s = 0
print("Minimum TSP cost:", tsp(graph, s))
