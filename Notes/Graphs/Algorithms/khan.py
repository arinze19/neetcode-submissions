from collections import deque

# Limitations: only works on DAG
def topological_sort(adjList, n):
    # initialise your indegree list
    indegree = [0] * n # O(v)
    order = []
    queue = deque([])
    
    for key in adjList: # O(v + e)
        for node in adjList[key]:
            indegree[node] += 1
            
    for i in range(len(indegree)): # O(v)
        if not indegree[i]:
            queue.append(i)
            
    while queue: # O(v)
        top = queue.popleft()
        
        order.append(top)
        
        for node in adjList[top]: # O(e)
            indegree[node] -= 1
            
            if not indegree[node]:
                queue.append(node)
                
    return order
        
            
adjList = {
    0: [1, 3],    
    1: [2],
    2: [],
    3: [1, 4, 5],
    4: [5],
    5: []
}

print(topological_sort(adjList, 6))
    
    
    
    