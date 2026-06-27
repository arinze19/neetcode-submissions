from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create a union-find (disjointed set)
        # update parents/components
        parents = [i for i in range(n)]
        count = 0

        def find(root):
            if root != parents[root]:
                parents[root] = find(parents[root])

            return parents[root]

        def union(nodeA, nodeB):
            rootA = find(nodeA)
            rootB = find(nodeB)

            if rootA == rootB:
                return False

            parents[rootA] = rootB
            return True

        for u, v in edges:
            union(u, v)

        for i in range(len(parents)):
            if parents[i] == i:
                count += 1

        return count