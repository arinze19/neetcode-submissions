from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        BRUTE FORCE
        Questions 
        1. No duplicate flights
        2. No flights from an airport to itself
        3. start and end
        4. would it be possible not to get there

        Thought process
        1. Directed graph | one way flights
        2. k | max number of stops to make

        - add items into an adjacency list 
        - loop through adjacency list and measure constraints

        Optimized 
        - create an adjacency list [done]
        1. BFS
            - base case (failure) [done]
                * stops > k
            - define base case (success) [done]
                * node == dst
            - keep track of the count of k
                * we can do that in the min-heap

        the reason we may want to rely on bellman ford here is because we have an amount we can travel (V)
        '''

        '''
        adjList = defaultdict(list)
        res = float("inf")
        heap = []
        visited = set()

        for source, destination, cost in flights:
            adjList[source].append((destination, cost))


        heap.append((0, src, 0)) # cost, src, stops

        while heap:
            cost, node, stops = heapq.heappop(heap)

            # print(node, cost, stops, adjList[node])

            if node in visited:
                continue

            if node == dst: # checking if we are at the end before checkinf for stops
                res = min(res, cost)
                continue

            if stops > k:
                continue

            visited.add(node)

            for next_destination, next_cost in adjList[node]:
                if next_destination not in visited:
                    heapq.heappush(heap, (next_cost + cost, next_destination, stops + 1))
        return -1
        '''
        shortest_paths = [float("inf")] * n

        shortest_paths[src] = 0
        
        for _ in range(k + 1): # +1 to account for the extra stop at the destination 
            snapshot = shortest_paths[:]

            for source, destination, cost in flights:
                if shortest_paths[source] + cost < snapshot[destination]:
                    snapshot[destination] = shortest_paths[source] + cost

            shortest_paths = snapshot[:]

        return shortest_paths[dst] if shortest_paths[dst] != float("inf") else -1

