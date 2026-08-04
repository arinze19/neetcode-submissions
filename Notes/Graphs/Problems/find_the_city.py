from collections import defaultdict 

def findTheCity(n, edges, distanceThreshold):
    '''
    Questions 
    1. Return the last city
    2. would we always have a least city? 

    Thought process 
    0. count | number of cities a node can reach
    0. current | node with the least
    1. initiate a nodes array | []
    2. create adjacency list 
    3. loop through each item in the adjacency list and run a dfs
    4.  dfs(node, count)
        - base case: if count <= distanceThreshold: add + 1 to arr[node]
        - loop through the children
    5. 

    Space and Time
    1. 
    '''
    arr = [0] * n
    adjList = defaultdict(list)
    res = -1
    

    for source, destination, cost in edges:
        adjList[source].append((destination, cost))
        adjList[destination].append((source, cost))

    def dfs(parent, node, count, visited):
        # base case
        if node in visited:
            return
        
        # add to visited
        visited.add(node)
        
        if node != parent:
            arr[parent] += 1
            
        print(parent, node, arr)
        
        for child, weight in adjList[node]:
            if child not in visited and count + weight <= distanceThreshold:
                dfs(parent, child, count + weight, visited)
        
        # remove current node from visited set (backtracking)

    for node in range(n): # Error: dictionary size changed during execution
        dfs(node, node, 0, set())
        

    count = min(arr)
    
    for i in range(n):
        if arr[i] <= count:
            res = i
            
    return res
        

# n = 4
# edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
# distanceThreshold = 4

n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2

# print(findTheCity(n, edges, distanceThreshold))