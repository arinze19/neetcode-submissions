'''
Union/Find
find(x) -> gets the parent of x
union(a, b) -> combines a and b

Union by rank
Union by no of children
'''

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # each node is its own parent initially
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            return False  # already connected → would create a cycle!
        
        self.parent[rootX] = rootY
        return True


graph = [[0, 1], [1, 2], [2, 3], [3, 1]]
n = 4

def detectCycle(graph, n):
    unionFind = UnionFind(n)

    for u, v in graph:
        if not unionFind.union(u, v):
            print("Union Cannot be found")
            return False
        
    return True

print(detectCycle(graph, n))
