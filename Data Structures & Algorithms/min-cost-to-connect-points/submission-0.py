from collections import defaultdict
import heapq 

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        Questions 
        1. points cannot be empty
        2. what to return if we're given only one point

        Thought process (sub problems)
        connect all points | adjacency list
        use djikstra to find the shortest path

        1. build adjacency list
        2. compute shortest path

        // 4, 2, 2, 4
        // djikstra

        Time and space complexity
        '''
        n = len(points)
        adjList = []
        parents = [node for node in range(n)]
        res = 0
        visited = set()

        for i in range(n):
            for j in range(i + 1, n):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adjList.append((i, j, weight))

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])

            return parents[x]

        def union(nodeA, nodeB):
            rootA = find(nodeA)
            rootB = find(nodeB)

            if rootA == rootB:
                return False

            parents[rootB] = rootA
            return True

        adjList.sort(key=lambda x: x[2])


        for source, destination, weight in adjList:
            if union(source, destination):
                res += weight

        return res

        
