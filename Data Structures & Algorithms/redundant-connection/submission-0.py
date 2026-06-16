from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        Questions
        1. can we have a situation where no answer is found?? No
        2. graph has only one cycle?? Yes

        Union-Find
        '''
        nodes = { i: i for i in range(1, len(edges) + 1) }
        
        def find(node):
            if nodes[node] != node:
                nodes[node] = find(nodes[node])

            return nodes[node]

        def union(node1, node2):
            rootNode1 = find(node1)
            rootNode2 = find(node2)

            if rootNode1 == rootNode2:
                return False

            nodes[rootNode1] = rootNode2
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []

        



