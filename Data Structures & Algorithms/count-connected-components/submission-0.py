from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # can edges be empty? no
        # n cannot be 0
        adjList = defaultdict(list)
        visited = set()
        count = 0

        for u, v in edges: # O(n)
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node):
            # base cas 
            if node in visited:
                return

            visited.add(node)

            for child in adjList[node]:
                dfs(child)

        for i in range(n): # O(n)
            if i not in visited:
                dfs(i)
                count += 1

        return count