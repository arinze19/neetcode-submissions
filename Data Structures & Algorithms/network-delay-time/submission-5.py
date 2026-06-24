import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        Thought process
        1. if is impossible if the number of nodes in visited != n
        '''
        # time | O(e) + O(v * logn)
        # space | O(v + e)
        heap = [(0, k)]
        adjList = { i: [] for i in range(1, n + 1) }
        visited = set()
        travelTimes = { node: float("inf") for node in range(1, n + 1) }
        res = 0

        for source, destination, time in times: # O(e)
            adjList[source].append((time, destination))

        while heap: # O(v)
            time, node = heapq.heappop(heap) # O(logn)

            if node in visited:
                continue 

            visited.add(node)

            res = time

            for childTime, childNode in adjList[node]:
                if childNode not in visited:
                    travelTimes[childNode] = min(travelTimes[childNode], time + childTime) 
                    heapq.heappush(heap, (time + childTime, childNode)) # O(logn)

        return res if len(visited) == n else -1
