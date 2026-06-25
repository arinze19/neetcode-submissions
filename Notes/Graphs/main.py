n = 4
edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]
adjList = { i: [] for i in range(n) }

for u, v in edges:
    adjList[u].append(v)
    adjList[v].append(u)

def canFinish(numCourses, prerequisites):
    # add to a adjList (DAG)
    adjList = { i: [] for i in range(numCourses) }
    visited = set()
    
    for u, v in prerequisites:
        adjList[v].append(u)
        
    def dfs(node):
        if node in visited:
            return False
        
        visited.add(node)
        
        for child in adjList[node]:
            if dfs(child):
                return False
            
        return True
        
    return dfs(0)
        
# prerequisites = [[0,1]]
prerequisites = [[0,1],[1,0]]

print(canFinish(2, prerequisites))
    

    