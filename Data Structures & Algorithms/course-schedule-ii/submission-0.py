class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # add to a adjList (DAG)
        adjList = { i: [] for i in range(numCourses) }
        indegree = [0] * numCourses # O(v)
        order = []
        queue = deque([])
        
        for u, v in prerequisites: # O(v + e)
            adjList[v].append(u)
            indegree[u] += 1
                
        for i in range(len(indegree)):
            if not indegree[i]:
                queue.append(i)
                
        while queue: # O(v)
            top = queue.popleft()
            
            order.append(top)
            
            for node in adjList[top]: # O(e)
                indegree[node] -= 1
                
                if not indegree[node]:
                    queue.append(node)
                    
        return order if len(order) == numCourses else []