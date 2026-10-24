class UnionFind:
    def __init__(self, n):
        self.parents = [num for num in range(n + 1)] # set up parents
        self.ranks = [0] * (n + 1) # set up ranks 
    def find(self, node_a):
        # find parent
        while self.parents[node_a] != node_a:
            node_a = self.parents[self.parents[node_a]] # path halving? log n

        return node_a

    def union(self, node_a, node_b):
        # find parent for both 
        # if connected return False 
        # if not connected 
        parent_a = self.find(node_a)
        parent_b = self.find(node_b)

        if parent_a == parent_b:
            return False 

        if self.ranks[parent_b] > self.ranks[parent_a]:
            parent_a, parent_b = parent_b, parent_a

        if self.ranks[parent_a] == self.ranks[parent_b]: # because there is an upper bound on the height of the Tree
            self.ranks[parent_a] += 1

        self.parents[parent_b] = parent_a

        return True
            
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        only one cycle exists 
        '''
        uf = UnionFind(len(edges)) # IF there exists only one cycle 

        for start, end in edges:
            parent_a = uf.find(start)
            parent_b = uf.find(end)

            if not uf.union(start, end):
                return [start, end]

        return [-1, -1]
