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

adj_list = [[0,1],[0,2], [1,2], [2,3]]
print(has_cycle(4, adj_list))
        
        