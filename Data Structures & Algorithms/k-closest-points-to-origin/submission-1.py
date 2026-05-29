import heapq
import math

# time - O(n * 2logk)
# space - O(k)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        # O(n)
        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2) 
            heapq.heappush(res, (-distance, [x,y])) # O(logk)
            if len(res) > k:
                heapq.heappop(res) # O(logk)

        for i in range(len(res)):
            res[i] = res[i][1]

        return res