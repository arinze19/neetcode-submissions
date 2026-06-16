from collections import defaultdict 

n = 4
edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]
adjList = { i: [] for i in range(n) }

for u, v in edges:
    adjList[u].append(v)
    adjList[v].append(u)

print(adjList)

    