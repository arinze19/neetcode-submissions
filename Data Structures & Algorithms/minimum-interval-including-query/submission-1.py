import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        BRUTE FORCE
        1. O(M * N) 
            - M: length of queries
            - N: length of intervals
        '''
        
        res = [-1] * len(queries)

        for i in range(len(queries)):
            count = float("inf")

            for start, end in intervals:
                if start <= queries[i] and queries[i] <= end:
                    count = min(end - start + 1, count)

            if count != float("inf"):
                res[i] = count

        return res

        '''
        OPTIMIZED
        1. dictionary + heap
        2. construct items based on if they fit criteria
        3. heapify the difference
        '''
        

        

