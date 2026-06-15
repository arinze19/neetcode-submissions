from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # for a tree to be valid
        # 1. no cycles 
        # 2. no isolated nodes
        adjList = defaultdict(list)
        visited = set()

        if not edges:
            return True

        if len(edges) >= n:
            return False

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node):
            # base case 
            if node not in adjList or node in visited:
                return

            visited.add(node)

            for child in adjList[node]:
                if child not in visited:
                    dfs(child)

        dfs(0)
        return len(visited) == n