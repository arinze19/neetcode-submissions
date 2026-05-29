import heapq
import math

# time - O(nlogk)
# space - O(k)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return the k closes points to the origin
        # create a new array that stores it as (distance, points)
        distances = []

        for coordinate in points: # O(n)
            distance = math.sqrt(coordinate[0] ** 2 + coordinate[1] ** 2)
            distances.append((distance, coordinate)) # O(1)
        
        # heapify
        heapq.heapify(distances) # O(n)

        res = heapq.nsmallest(k, distances) # O(nlogk)

        for i in range(len(res)): # O(n)
            res[i] = res[i][1]

        return res