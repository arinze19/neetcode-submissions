'''
Union/Find
find(x) -> gets the parent of x
union(a, b) -> combines a and b
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


uf = UnionFind(6)  # nodes 0,1,2,3,4,5

print(uf.union(0, 1))  # True  → merges 0 and 1
print(uf.union(2, 3))  # True  → merges 2 and 3
print(uf.union(1, 2))  # True  → merges {0,1} with {2,3}

print(uf.find(0) == uf.find(3))  # True ✅ same group now!
print(uf.find(0) == uf.find(4))  # False ❌ different groups

print(uf.union(0, 3))  # False ❌ already connected → cycle detected!
