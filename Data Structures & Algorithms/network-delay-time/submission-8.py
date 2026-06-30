import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        1. ensure the nodes are wholly connected
        '''
        shortest_paths = { node: float("inf") for node in range(1, n + 1) }
        shortest_paths[k] = 0
        res = 0

        for _ in range(n - 1):
            for source, destination, weight in times:
                if shortest_paths[source] + weight < shortest_paths[destination]:
                    shortest_paths[destination] = shortest_paths[source] + weight

        # confirm for negative edge weights and if nodes are not fully connected 
        for source, destination, weight in times:
            if shortest_paths[source] + weight < shortest_paths[destination]:
                return -1 

        for node, time in shortest_paths.items():
            res = max(res, time)

        return res if res != float("inf") else -1