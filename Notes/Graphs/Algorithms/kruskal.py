'''
Constraints 
1. Does not work for directed graphs
'''
def kruskal(edges, n):
    parents = [i for i in range(n)]
    edges.sort(key=lambda x: x[2])
    res = []
    
    def find(root):
        if root != parents[root]:
            parents[root] = find(parents[root])
            
        return parents[root]
    
    def union(nodeA, nodeB):
        rootA = find(nodeA)
        rootB = find(nodeB)
        
        if rootA == rootB:
            return False
        
        parents[rootB] = rootA 
        return True
    
    for u, v, weight in edges:
        if union(u, v):
            res.append([u, v, weight])
            
    return res
    
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

print(kruskal(edges, n))