import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # result should be sorted in ascending order 
        # if a < x == b - x | priority to a < b
        heap = []
        res = []

        # O(n)
        for num in arr:
            heap.append((abs(num - x), num))

        # O(n)
        heapq.heapify(heap)

        #O(nlogk)
        res = [item[1] for item in heapq.nsmallest(k, heap)]

        
        # O(klogk)
        res.sort()

        return res
