import random
import heapq

def prims(edges, n):
    # build our adjacency list
    adjList = [[] for i in range(n)]
    res = []
    count = 0
    heap = []
    visited = set()
    
    for source, destination, weight in edges:
        adjList[source].append((destination, weight))
        adjList[destination].append((source, weight))
        
    # starting from a random node
    heap.append((0, random.randint(0, len(adjList) - 1)))
    
    while heap:
        weight, node = heapq.heappop(heap)
        
        if node in visited:
            continue
        
        visited.add(node)
        res.append(node)
        count += weight
        
        for neighborNode, neighborWeight in adjList[node]:
            if neighborNode not in visited:
                heapq.heappush(heap, (neighborWeight, neighborNode))
    
    return res, count
    
    
edges = [
    [0, 1, 4],
    [0, 2, 2],
    [1, 2, 5],
    [1, 3, 10],
    [2, 4, 3],
    [4, 3, 4],
    [3, 5, 11],
    [4, 5, 6],
]

n = 6

print(prims(edges, n))