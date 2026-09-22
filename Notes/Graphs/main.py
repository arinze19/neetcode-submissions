n = 4
edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]
adjList = [[] for _ in range(n)]

for u, v in edges:
    adjList[u].append(v)
    adjList[v].append(u)

def canFinish(numCourses, prerequisites):
    # add to a adjList (DAG)
    adjList = [[] for _ in range(numCourses) ]
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


# --------------------------------------------

'''
This is the form to reach for whenever the problem says "n nodes labelled 0 to n−1". 
Indexing a list is faster than hashing, and isolated vertices are handled for free.
'''

def build_from_n(n, edges):
    # every vertex has a slot, even isolated ones
    # arrays are better for operations than hash tables
    # integer vertices
    graph = [[] for _ in range(n)] 
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

# --------------------------------------------

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []
 
    while stack:
        # take from the TOP
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for nbr in graph[node]:
            if nbr not in visited:
                stack.append(nbr)
    return order
    

    