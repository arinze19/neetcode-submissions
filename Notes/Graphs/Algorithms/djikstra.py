import heapq 

# space | O(V + E)
# time | O(E log V)
def djikstra(times, start, no_of_nodes):
    heap = [(0, start)]
    visited = set()
    adjList = { i: [] for i in range(1, no_of_nodes + 1) }
    travelTimes = { i: float("inf") for i in range(1, no_of_nodes + 1) }
    
    # Build adjacency list 
    for source, destination, weight in times: 
        adjList[source].append((weight, destination))
        
    travelTimes[start] = 0
        
    # build your queue logic
    while heap: 
        weight, node = heapq.heappop(heap) 
        
        visited.add(node) 
        
        for childWeight, childNode in adjList[node]: 
            if childNode not in visited:
                travelTimes[childNode] = min(travelTimes[childNode], weight + childWeight)
                heapq.heappush(heap, (weight + childWeight, childNode)) 
    
    return travelTimes[no_of_nodes]
    
times = [
    [1, 2, 9],
    [1, 4, 2],
    [2, 5, 1],
    [4, 2, 4],
    [4, 5, 6],
    [3, 2, 3],
    [5, 3, 7],
    [3, 1, 5],
]
n = 5
k = 1

print(djikstra(times, k, n))