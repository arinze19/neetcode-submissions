from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # how to construct the adjList
        adjList = { i: [] for i in range(numCourses) }
        indegrees = [0] * numCourses
        queue = deque([])
        count = 0

        for u, v in prerequisites:
            adjList[v].append(u)

            indegrees[u] += 1

        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)


        while queue:
            top = queue.popleft()
            count += 1

            for node in adjList[top]:
                indegrees[node] -= 1

                if not indegrees[node]:
                    queue.append(node)

        return count == numCourses
