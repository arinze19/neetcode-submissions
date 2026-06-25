# time | O(V * E)
# space | O(V)
def bellmanFord(paths, start, no_of_nodes):
    travelTimes = { node: float("inf") for node in range(1, no_of_nodes + 1)}
    
    travelTimes[start] = 0
    
    for _ in range(no_of_nodes - 1):
        for source, destination, weight in paths:
            if weight + travelTimes[source] < travelTimes[destination]:
                travelTimes[destination] = weight + travelTimes[source]
                
    for source, destination, weight in paths:
        if weight + travelTimes[source] < travelTimes[destination]:
            return False
                
    return travelTimes
        
paths = [
    [1, 4, 7],
    [1, 2, 5],
    [1, 3, 6],
    [2, 4, -3],
    [3, 4, -2]
]

start = 1
no_of_nodes = 4

bellmanFord(paths, start, no_of_nodes)
    