def has_cycle(n, edges):
    # build your adjacency list 
    adj_list = [[] for _ in range(n)]
    visited = set()
    
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    for node in range(n):
        if node not in visited:
            visited.add(node)
            stack = [(node, -1)] # -1 indicates that there is not parent for this node
            while stack:
                current, parent = stack.pop()
                
                for neighbour in adj_list[current]:
                    if neighbour == parent:
                        continue 
                    
                    if neighbour in visited:
                        return True 
                    
                    visited.add(neighbour)
                    stack.append((neighbour, current))   # [(1, 0), (2, 0)]                  
    
    return False

# ------------------------------------------

# 3-state DFS
def can_finish(n, edges):
    # build adjacency list 
    adj_list = [[] for _ in range(n)]
    state = ["unseen"] * n
    
    for req, prereq in edges:
        adj_list[prereq].append(req)
        
    def has_cycle(node):
        # base case 
        if state[node] == "visited":
            return True
        
        state[node] = "visited"
        
        # loop through the children
        for child in adj_list[node]:
            if state[child] == "visited":
                return True
            
            if state[child] == "unseen" and has_cycle(child):
                return True
            
        state[node] = "done"
            
        return False 
    
    # dfs through the adjacency list 
    for node in range(n):
       if state[node] == "unseen" and has_cycle(node):
           return False 
       
    return True

# edges = [[1,0], [2,0], [0,2], [3,2]]
edges = [[0,0]]
n = 1
print(can_finish(n, edges))
    
        
        