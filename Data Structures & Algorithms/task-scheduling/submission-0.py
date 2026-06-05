import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        candidates = Counter(tasks) # O(n)

        heap = []
        queue = deque([])
        res = 0

        for key in candidates: # O(n)
            heap.append((-candidates[key], key))

        heapq.heapify(heap) # O(n)

        while heap or queue: # O(M(delay) * n)
            if heap:
                count, value = heapq.heappop(heap) # O(1)
                count += 1

                if count:
                    queue.append((res + n, count, value)) #O(1)

            if queue and queue[0][0] <= res:
                delay, count, char = queue.popleft() #O(1)
                heapq.heappush(heap, (count, char)) # O(logn)

            res += 1

        return res

        

